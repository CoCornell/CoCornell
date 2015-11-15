from flask import redirect, url_for
from flask.ext.login import logout_user

from mysite import app


@app.route('/signout/', methods=['GET'])
def signout():
    logout_user()
    return redirect(url_for("index"))
