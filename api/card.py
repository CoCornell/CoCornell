# encoding: utf-8
from flask import request, g

from mysite.models.list import List
from mysite.models.card import Card
from mysite.models.ocr import OCR
from mysite.api import api
from mysite.api.token import auth
from mysite.api.const import Error
from mysite.api.utils import ok, error


@api.route("/card/<int:card_id>/", methods=['DELETE'])
@auth.login_required
def delete_card(card_id):
    """
    Deletes the card specified by card_id.
    """
    if not Card.has_access_to(g.user.netid, card_id):
        return error(Error.NO_ACCESS_TO_CARD)

    Card.delete_card_by_id(card_id)
    return ok({"deleted": True})


@api.route("/card/", methods=['POST'])
@auth.login_required
def add_card():
    """
    Adds a card specified by card content and list id.
    Returns the created card id.
    """
    content = request.form.get("content")
    list_id = request.form.get("list_id")

    if not content:
        return error(Error.EMPTY_CONTENT, 400)
    elif not list_id:
        return error(Error.EMPTY_LIST_ID, 400)

    if not List.has_access_to(g.user.netid, list_id):
        return error(Error.NO_ACCESS_TO_BOARD, 400)

    card = Card.add_card(list_id, content)
    return ok({"created": True, "list": card.to_dict()})


@api.route("/card/<int:card_id>/ocr-text/", methods=['GET'])
@auth.login_required
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
