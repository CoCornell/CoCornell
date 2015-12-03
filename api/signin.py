from flask import request

from mysite.api import api
from mysite.api.utils import error, ok
from mysite.api.const import Error
from mysite.models.user import User


@api.route("/signin/", methods=['POST'])
def signin():
    netid = request.form.get('netid', '').strip()
    password = request.form.get('password', '').strip()

    if not netid:
        return error(Error.EMPTY_NETID)

    if not password:
        return error(Error.EMPTY_PASSWORD)

    registered_user = User.get_user(netid)

    if not registered_user:
        return error(Error.NETID_NOT_EXIST)

    if not registered_user.check_password(password):
        return error(Error.INVALID_PASSWORD)

    ret = registered_user.to_dict()
    ret.pop("password")

    return ok(ret)
