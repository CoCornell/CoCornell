from flask import g

from mysite.api.token import auth
from mysite.models.user import User


@auth.verify_password
def check_password(netid_or_token, password):
    # first try to authenticate by token
    user = User.verify_auth_token(netid_or_token)
    if not user:
        # try to authenticate with netid/password
        user = User.query.filter_by(netid=netid_or_token).first()
        if not user or not user.check_password(password):
            return False
    g.user = user
    return True
