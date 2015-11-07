from flask import request, render_template, g
from flask.ext.login import login_required

from mysite import app
from mysite.models.user import User


@app.route('/board', methods=['GET'])
@login_required
def board():
    return render_template("board.html")
