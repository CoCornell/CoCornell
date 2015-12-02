from flask import g

from mysite.api import api
from mysite.models.board import Board
from mysite.api.utils import ok
from mysite.api.token import auth


@api.route('/board/', methods=['GET'])
@auth.login_required
def board():
    """
    Returns all the boards the user has access to.
    """
    board_ids = Board.get_board_ids_by_netid(g.user.netid)
    boards = map(lambda id_: Board.get_board_by_id(id_).to_dict(), board_ids)
    return ok({'boards': boards})


@api.route('/board/count/', methods=['GET'])
@auth.login_required
def board_count():
    """
    Returns number of boards the user has access to.
    """
    count = Board.get_board_count_by_netid(g.user.netid)
    return ok({'count': count})
