from werkzeug.security import generate_password_hash, check_password_hash
from flask import g, redirect, flash
from flask.ext.login import UserMixin, current_user
from datetime import datetime
from mysite import app, db, login_manager
from mysite.models import SerializableModel


class User(db.Model, SerializableModel, UserMixin):
    __tablename__ = 'user'

    netid = db.Column(db.String(10), primary_key=True)
    password = db.Column(db.String(250))
    name = db.Column(db.String(50))
    reg_time = db.Column(db.DATETIME, default=datetime.utcnow)

    def __init__(self, netid, password, name):
        self.netid = netid
        self.set_password(password)
        self.name = name
        self.reg_time = datetime.now()

    def __repr__(self):
        return '<User [%s], %s>' % (self.netid, self.name)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.netid)

    def __unicode__(self):
        return self.netid

    @classmethod
    def get_user(cls, netid):
        return db.session.query(User).get(netid)

    @classmethod
    def add_user(cls, netid, password, name):
        user = User(netid, password, name)
        db.session.add(user)
        db.session.commit()


@login_manager.user_loader
def load_user(netid):
    return User.get_user(netid)


@app.before_request
def before_request():
    g.user = current_user


@login_manager.unauthorized_handler
def unauthorized_callback():
    flash("Please sign in first.")
    return redirect('/signin')
