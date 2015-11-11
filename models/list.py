from mysite import db
from mysite.models import SerializableModel
from mysite.models.card import Card


class List(db.Model, SerializableModel):

    __tablename__ = 'list'

    id = db.Column(db.Integer, primary_key=True)
    board_id = db.Column(db.Integer)
    name = db.Column(db.String(50))

    def __init__(self, board_id, name):
        self.board_id = int(board_id)
        self.name = name

    def __repr__(self):
        return '<List [%d], %d, %s>' % (self.id, self.board_id, self.name)

    @classmethod
    def get_cards_by_list_id(cls, list_id):
        return list(Card.query.filter_by(list_id=list_id))

    @classmethod
    def add_list(cls, board_id, name):
        """
        Adds a list to the board.
        """
        new_list = List(board_id, name)
        db.session.add(new_list)
        db.session.commit()
