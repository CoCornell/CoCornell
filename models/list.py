from mysite import db
from mysite.models import SerializableModel


class List(db.Model, SerializableModel):

    __tablename__ = 'list'

    id = db.Column(db.Integer, primary_key=True)
    board_id = db.Column(db.Integer)
    name = db.Column(db.String(50))

    def __init__(self, board_id, name):
        self.board_id = int(board_id)
        self.name = name

    def __repr__(self):
        return '<List [%d], self.name>' % (self.id, self.name)
