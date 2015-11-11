from flask import request, render_template, flash, redirect, url_for
from flask.ext.login import login_user

from mysite import app
from mysite.models.user import User


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'GET':
        return render_template("signin.html")

    netid = request.form['netid']
    password = request.form['password']
    remember_me = 'remember_me' in request.form

    registered_user = User.get_user(netid)

    if not registered_user:
        flash('NetID does not exist.')
        return redirect(url_for('signin'))

    assert isinstance(registered_user, User)

    if not registered_user.check_password(password):
        flash('Wrong password')
        return redirect(url_for('signin'))

    login_user(registered_user, remember_me)
    flash('Login successfully')
    return redirect(url_for('index'))
