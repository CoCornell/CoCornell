from flask import render_template, redirect, url_for, g

from mysite import app
from mysite.models.user import User
from mysite.models.board import Board


@app.route('/')
def index():
    if g.user.is_authenticated:
        return redirect(url_for('board'))

    return render_template('index.html')
