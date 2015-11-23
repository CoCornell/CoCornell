from flask import g, jsonify
from mysite.api import api
from mysite.models.board import Board
from mysite.api.utils import ok
from mysite.api.token import auth


@api.route('/board/', methods=['GET'])
@auth.login_required
def board():
    board_ids = Board.get_board_ids_by_netid(g.user.netid)
    boards = map(lambda id: Board.get_board_by_id(id).to_dict(), board_ids)
    return ok({'boards': boards})


@api.route('/board/count/', methods=['GET'])
@auth.login_required
def board_count():
    count = Board.get_board_count_by_netid(g.user.netid)
    return ok({'count': count})
