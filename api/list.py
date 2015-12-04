from flask import request, g

from mysite.models.board import Board
from mysite.models.list import List
from mysite.api import api
from mysite.api.token import auth
from mysite.api.const import Error
from mysite.api.utils import ok, error


@api.route("/board/<int:board_id>/list/", methods=['GET'])
@auth.login_required
def board_lists(board_id):
    """
    Returns all the lists belongs to the board specified by board id.
    """
    if not Board.has_access_to(g.user.netid, board_id):
        return error(Error.NO_ACCESS_TO_BOARD)

    lists = List.get_lists_by_board_id(board_id)
    return ok({"lists": map(lambda x: x.to_dict(), lists)})


@api.route("/list/<int:list_id>/", methods=['GET', 'DELETE'])
@auth.login_required
def list_(list_id):
    """
    Returns or deletes the list specified by list id.
    """
    if not List.has_access_to(g.user.netid, list_id):
        return error(Error.NO_ACCESS_TO_LIST)

    if request.method == 'GET':
        l = List.get_list_by_id(list_id).to_dict()
        cards = List.get_cards_by_list_id(list_id)
        l['cards'] = map(lambda x: x.to_dict(), cards)
        return ok({"list": l})

    if request.method == 'DELETE':
        List.delete_list_by_id(list_id)
        return ok({"deleted": True})


@api.route("/list/", methods=['POST'])
@auth.login_required
def add_list():
    """
    Adds a list specified by list name and board id.
    Returns the created list id.
    """
    list_name = request.form.get("list_name")
    board_id = request.form.get("board_id")
    if not list_name or not board_id:
        return error()
