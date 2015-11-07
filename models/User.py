from werkzeug.security import generate_password_hash, check_password_hash
from flask.ext.login import UserMixin

from datetime import datetime

from mysite import db
from mysite.models import SerializableModel


class User(db.Model, SerializableModel, UserMixin):
    __tablename__ = 'user'

    netid = db.Column(db.String(10), primary_key=True)
    password = db.Column(db.String(250))
    name = db.Column(db.String(50))
    reg_time = db.Column(db.DATETIME, default=datetime.utcnow)

    def __init__(self, netid, password, name):
        assert 5 <= len(netid) < 10
        assert 0 < len(name) <= 50

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
        return self.username

