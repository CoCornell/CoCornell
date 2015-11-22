from flask import request

from mysite.api import api
from mysite.api.utils import ok, error
from mysite.api.const import Error
from mysite.models.user import User


@api.route('/signup/', methods=['POST'])
def signup():
    netid = request.form.get('netid', '')
    password = request.form.get('password', '')
    name = request.form.get('name', '')

    if not netid:
        return error(Error.EMPTY_NETID, 400)
    if not password:
        return error(Error.EMPTY_PASSWORD, 400)
    if not name:
        return error(Error.EMPTY_NAME, 400)

    if User.get_user(netid):
        return error(Error.NETID_EXISTED, 400)

    user = User.add_user(netid, password, name)
    ret = user.to_dict()
    ret.pop("password")

    return ok({"user": ret})
