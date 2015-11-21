from flask import request

from mysite.api import api
from mysite.api.utils import error, ok
from mysite.models.user import User


@api.route("/signin/", methods=['GET', 'POST'])
def signin():
    netid = request.form.get('netid', '').strip()
    password = request.form.get('password', '').strip()

    if not netid:
        return error("EMPTY_NETID", "netid should not be empty")

    if not password:
        return error("EMPTY_PASSWORD", "password should not be empty")

    registered_user = User.get_user(netid)

    if not registered_user:
        return error("USER_NOT_EXIST", "netid does not exist")

    if not registered_user.check_password(password):
        return error("INVALID_PASSWORD", "invalid password")

    ret = registered_user.to_dict()
    ret.pop("password")

    return ok(ret)
