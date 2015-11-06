from datetime import datetime

from mysite import db
from mysite.models import SerializableModel


class User(db.Model, SerializableModel):
    __tablename__ = 'user'

    netid = db.Column(db.String(10), primary_key=True)
    name = db.Column(db.String(50))
    reg_time = db.Column(db.DATETIME, default=datetime.utcnow)

    def __init__(self, netid, name):
        assert 5 <= len(netid) < 10
        assert 0 < len(name) <= 50

        self.netid = netid
        self.name = name
        self.reg_time = datetime.now()

    def __repr__(self):
        return '<User [%s], %s>' % (self.netid, self.name)
