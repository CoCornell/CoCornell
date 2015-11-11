from flask import g, request, flash, redirect, render_template

from mysite import app
from mysite.models.list import List
from mysite.models.board import Board


@app.route("/list", methods=['POST'])
def list():
    board_id_temp = request.referrer.split('/')[-1]
    board_id = ""
    for c in board_id_temp:
        if c.isdigit():
            board_id += c
        else:
            break
    if not Board.has_access_to(g.user.netid, board_id):
        return render_template("no_access.html")
    name = request.form.get('name')
    if not name:
        flash("List name can not be empty.")
        return redirect('/board/' + board_id)
    List.add_list(board_id, name)
    return redirect('/board/' + board_id)
