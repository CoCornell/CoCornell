from flask import request, render_template, flash, redirect, url_for, g
from flask.ext.login import login_user

from mysite import app
from mysite.models.user import User
from mysite.api.utils import ok, error
from mysite.api.const import Error


@app.route('/signin/', methods=['GET', 'POST'])
def signin():
    if g.user.is_authenticated:
        return redirect(url_for('board'))

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
    return redirect(url_for('board'))


@app.route('/signin2/', methods=['POST'])
def signin2():
    """
    Used as REST API.
    """
    netid = request.form['netid'].strip()
    password = request.form['password'].strip()
    remember_me = 'remember_me' in request.form

    registered_user = User.get_user(netid)

    if not registered_user:
        return error(Error.NETID_NOT_EXIST)

    if not registered_user.check_password(password):
        return error(Error.INVALID_PASSWORD)

    login_user(registered_user, remember_me)

    ret = registered_user.to_dict()
    ret.pop("password")

    return ok(ret)
