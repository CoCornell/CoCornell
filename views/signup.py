from flask import request, render_template, redirect, flash, url_for

from mysite import app
from mysite.models.user import User


@app.route("/signup/", methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template("signup.html")

    netid = request.form['netid']
    password = request.form['password']
    name = request.form['name']

    if not netid or not password or not name:
        flash("Please fill all the blanks.")

    if User.get_user(netid):
        flash(u'NetID already exists!')
        return redirect(url_for('signin'))

    User.add_user(netid, password, name)
    flash('Sign up successfully.')
    return redirect(url_for('signin'))
