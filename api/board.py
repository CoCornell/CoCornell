from flask import g, request

from mysite.api import api
from mysite.models.board import Board
from mysite.models.access import Access
from mysite.models.list import List
from mysite.api.utils import ok, error
from mysite.api.token import auth
from mysite.api.const import Error


@api.route('/board/', methods=['GET', 'POST'])
@auth.login_required
def all_boards():
    """
    Returns all the boards the user has access to
    or adds a board.
    """
    if request.method == 'GET':
        board_ids = Board.get_board_ids_by_netid(g.user.netid)
        boards = map(lambda id_: Board.get_board_by_id(id_).to_dict(), board_ids)
        return ok({'boards': boards})

    elif request.method == 'POST':
        # add a board
        board_name = request.form.get("name")

        if not board_name:
            return error(Error.EMPTY_BOARD_ID, 400)

        b = Board.add_board(board_name)
        Access.add_access(b.id, g.user.netid)
        return ok({"created": True, "board": b.to_dict()})


@api.route('/board/count/', methods=['GET'])
@auth.login_required
def board_count():
    """
    Returns number of boards the user has access to.
    """
    count = Board.get_board_count_by_netid(g.user.netid)
    return ok({'count': count})


@api.route('/board/<int:board_id>/', methods=['GET'])
@auth.login_required
def board(board_id):
    """
    Returns all the lists of the board specified by board_id.
    """
    lists = List.get_lists_by_board_id(board_id)
    lists = map(lambda x: x.to_dict(), lists)
    return ok({'lists': lists})
