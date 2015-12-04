from mysite import db
from mysite.models import SerializableModel
from mysite.models.board import Board
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
    def get_list_by_id(cls, list_id):
        return List.query.filter_by(id=list_id).first()

    @classmethod
    def has_access_to(cls, netid, list_id):
        """
        Returns if user has access to the list.
        """
        list_ = List.get_list_by_id(list_id)
        return Board.has_access_to(netid, list_.board_id) if list_ else False

    @classmethod
    def has_access_to_card(cls, netid, card_id):
        """
        Returns if user has access to the card.
        """
        card = Card.get_card_by_id(card_id)
        return List.has_access_to(netid, card.list_id)

    @classmethod
    def get_cards_by_list_id(cls, list_id):
        """
        Returns all cards belong to the list.
        """
        return list(Card.query.filter_by(list_id=list_id))

    @classmethod
    def add_list(cls, board_id, name):
        """
        Adds a list to the board.
        """
        new_list = List(board_id, name)
        db.session.add(new_list)
        db.session.commit()

    @classmethod
    def get_lists_by_board_id(cls, board_id):
        return list(List.query.filter_by(board_id=board_id))

    @classmethod
    def delete_list_by_id(cls, list_id):
        db.session.query(List).filter(List.id == list_id).delete()
        db.session.commit()
