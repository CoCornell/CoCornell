from flask import render_template
from mysite import app, db
from mysite.models.user import User


@app.route('/')
def index():
    users = User.query.with_entities(User.netid, User.name, User.reg_time)
    for user in users:
        print user
    return render_template('index.html')
