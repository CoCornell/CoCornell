from flask import render_template

from mysite import app
from mysite.models.user import User
from mysite.models.board import Board


@app.route('/')
def index():
    users = User.query.with_entities(User.netid, User.name, User.reg_time)
    boards = Board.query.with_entities(Board.id, Board.name)
    return render_template('index.html')
