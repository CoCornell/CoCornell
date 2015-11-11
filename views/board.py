from flask import request, render_template, g, flash, redirect, url_for
from flask.ext.login import login_required

from mysite import app
from mysite.models.board import Board


@app.route('/board', methods=['GET', 'POST'])
@login_required
def board():
    if request.method == 'GET':
        board_ids = Board.get_board_ids_by_netid(g.user.netid)
        return render_template("board.html", board_ids=board_ids)
    else:
        # request.method == 'POST'
        name = request.form.get('name')
        if not name:
            flash("Board name can not be empty.")
            return redirect(url_for('board'))
        Board.add_board(name)
        return redirect(url_for('board'))


@app.route("/board/<int:board_id>", methods=['GET'])
@login_required
def board_page(board_id):
    """
    Main page of the board.
    """
    if not Board.has_access_to(g.user.netid, board_id):
        return render_template("no_access.html")
    lists = Board.get_lists_by_board_id(board_id)
    return render_template("board_page.html", lists=lists)
