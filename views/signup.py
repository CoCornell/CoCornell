from flask import request, render_template, redirect, flash, url_for

from mysite import app, db
from mysite.models.user import User


@app.route("/signup")
def signup():
    if request.method == 'GET':
        return render_template("signup.html")

    session = db.session

    netid = request.form['netid']
    password = request.form['password']
    name = request.form['name']

    if not netid or not password or not name:
        flash("Please fill all the blanks.")

    if session.query(User).get(netid):
        flash(u'NetID already exists!')
        return redirect(url_for('index'))

    user = User(netid, password, name)
    session.add(user)
    session.commit()
    session.close()
    flash('Sign up successfully.')
    return redirect(url_for('signin'))
