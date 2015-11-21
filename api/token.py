from flask import g, jsonify
from flask.ext.httpauth import HTTPBasicAuth

from mysite.api import api


auth = HTTPBasicAuth()


@api.route('/token/')
@auth.login_required
def get_auth_token():
    token = g.user.generate_auth_token()
    return jsonify({'token': token.decode('ascii')})
