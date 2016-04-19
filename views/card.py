from flask import g, request, flash, redirect, render_template, url_for, jsonify
from flask.ext.login import login_required

from mysite import app
from mysite.models.list import List
from mysite.models.card import Card
from mysite.models.ocr import OCR
from mysite.api.utils import ok, error
from mysite.api.const import Error


@app.route("/card/", methods=['POST'])
@login_required
def add_card():
    """
    Adds a card to a list.
    """
    list_id = request.form.get("list_id")
    if not list_id:
        return redirect(url_for("board"))

    board_id = List.get_list_by_id(list_id).board_id

    if not List.has_access_to(g.user.netid, list_id):
        return render_template("no_access.html")

    content = request.form.get("content")
    if not content:
        flash("Card content can not be empty.")
    else:
        Card.add_card(list_id, content)
    return redirect('/board/' + str(board_id))


@app.route("/card/<int:card_id>/", methods=['DELETE'])
@login_required
def delete_card(card_id):
    """
    Deletes a card.
    """
    if not List.has_access_to_card(g.user.netid, card_id):
        return redirect(url_for('board'))
    Card.delete_card_by_id(card_id)
    return jsonify({"deleted": True})


@app.route("/card/<int:card_id>/ocr-text/", methods=['GET'])
@login_required
def card_ocr_text(card_id):
    """
    Returns the OCR text of a card if it is an image card.
    """
    ocr = OCR.get_ocr_by_card_id(card_id)
    if not ocr:
        return error(Error.NO_OCR_TEXT)
    return ok({
        "ocr": {
            "card_id": ocr.card_id,
            "text": ocr.text
        }
    })
