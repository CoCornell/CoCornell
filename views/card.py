from flask import g, request, flash, redirect, render_template, url_for
from flask.ext.login import login_required

from mysite import app
from mysite.models.list import List
from mysite.models.card import Card


@app.route("/card/<int:list_id>/", methods=['POST'])
@login_required
def add_card(list_id):
    """
    Adds a card to a list.
    """
    board_id = List.get_list_by_id(list_id).board_id

    if not List.has_access_to(g.user.netid, list_id):
        return render_template("no_access.html")

    content = request.form.get("content")
    if not content:
        flash("Card content can not be empty.")
    else:
        Card.add_card(list_id, content)
    return redirect('/board/' + str(board_id))
