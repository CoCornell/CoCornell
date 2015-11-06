from mysite import db
from mysite.models import SerializableModel


class Board(db.Model, SerializableModel):

    __tablename__ = 'board'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Board [%d], %s>' % (self.id, self.name)
