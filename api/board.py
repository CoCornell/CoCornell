from flask.ext.login import login_required

from mysite.api import api
from mysite.models.board import Board
from mysite.api.utils import ok
from mysite.api.token import auth


@api.route('/board/', methods=['GET'])
@auth.login_required
def board():
    return ok("this is ok")
