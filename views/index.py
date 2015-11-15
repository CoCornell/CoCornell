from flask import render_template

from mysite import app
from mysite.models.user import User
from mysite.models.board import Board


@app.route('/')
def index():
    return render_template('index.html')
