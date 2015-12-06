from mysite import db
from mysite.models import SerializableModel


class Access(db.Model, SerializableModel):

    __tablename__ = 'access'

    board_id = db.Column(db.Integer, primary_key=True)
    netid = db.Column(db.String(10), primary_key=True)

    def __init__(self, board_id, netid):
        self.board_id = int(board_id)
        self.netid = netid

    def __repr__(self):
        return '<Access board %s, netid %s>' % (self.board_id, self.netid)

    @classmethod
    def add_access(cls, board_id, netid):
        try:
            access = Access(board_id, netid)
            db.session.add(access)
            db.session.commit()
            return True
        except:
            db.session.rollback()
            return False
