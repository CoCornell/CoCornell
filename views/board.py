from flask import request, render_template, g, flash, redirect, url_for, jsonify
from flask.ext.login import login_required

from mysite import app
from mysite.models.board import Board
from mysite.models.list import List
from mysite.api.utils import error, ok
from mysite.api.const import Error


@app.route('/board/', methods=['GET', 'POST'])
@login_required
def board():
    if request.method == 'GET':
        board_ids = Board.get_board_ids_by_netid(g.user.netid)
        boards = map(Board.get_board_by_id, board_ids)
        return render_template("board.html", boards=boards)
    else:
        # request.method == 'POST'
        name = request.form.get('name')
        if not name:
            flash("Board name can not be empty.")
            return redirect(url_for('board'))
        Board.add_board(name)
        return redirect(url_for('board'))


@app.route("/board/<int:board_id>/", methods=['GET'])
@login_required
def board_page(board_id):
    if not Board.has_access_to(g.user.netid, board_id):
        return render_template("no_access.html")
    lists = List.get_lists_by_board_id(board_id)
    return render_template("board_page.html", lists=lists)


@app.route("/board/<int:board_id>/list/", methods=['GET', 'POST'])
@login_required
def board_list(board_id):
    """
    GET: get all lists of the specified board
    POST: add a list to the specified board

    Return JSON.
    """
    if request.method == 'GET':
        lists = List.get_lists_by_board_id(board_id)
        return ok({"lists": map(lambda x: x.to_dict(), lists)})
    elif request.method == 'POST':
        name = request.form.get("name")
        if not name:
            return error(Error.EMPTY_LIST_NAME, 400)

        if not Board.has_access_to(g.user.netid, board_id):
            return error(Error.NO_ACCESS_TO_BOARD, 400)

        list_ = List.add_list(board_id, name)
        return ok({"created": True, "list": list_.to_dict()})
