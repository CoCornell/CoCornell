from mysite import db
from mysite.models import SerializableModel


class List(db.Model, SerializableModel):

    __tablename__ = 'access'

    id = db.Column(db.Integer, primary_key=True)
    board_id = db.Column(db.Integer)
    netid = db.Column(db.String(10))

    def __init__(self, board_id, netid):
        self.board_id = int(board_id)
        self.netid = netid

    def __repr__(self):
        return '<Access [%d], board %s, netid %s>' % (self.id, self.board_id, self.netid)
