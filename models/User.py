from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, SignatureExpired, BadSignature
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
        return user

    @classmethod
    def delete_user(cls, netid):
        user = cls.get_user(netid)
        db.session.delete(user)
        db.session.commit()

    def generate_auth_token(self, expiration=600):
        s = Serializer(app.config['SECRET_KEY'], expires_in=expiration)
        return s.dumps({ 'netid': self.netid })

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None  # valid token, but expired
        except BadSignature:
            return None  # invalid token
        user = User.query.get(data['netid'])
        return user


@login_manager.user_loader
def load_user(netid):
    return User.get_user(netid)


@app.before_request
def before_request():
    g.user = current_user


@login_manager.unauthorized_handler
def unauthorized_callback():
    flash("Please sign in first.")
    return redirect('/signin/')
