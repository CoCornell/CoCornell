from flask import g

from mysite import db
from mysite.models import SerializableModel
from mysite.models.access import Access
from mysite.models.list import List


class Board(db.Model, SerializableModel):

    __tablename__ = 'board'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Board [%d], %s>' % (self.id, self.name)

    @classmethod
    def get_board_by_id(cls, id):
        """
        Returns the board specified by id.
        """
        return Board.query.filter_by(id=id)[0]

    @classmethod
    def get_board_ids_by_netid(cls, netid):
        """
        Returns id of boards accessible to the user specified by the netid.
        """
        return map(lambda t: int(t[0]), Access.query.filter_by(netid=netid).with_entities(Access.board_id))

    @classmethod
    def has_access_to(cls, netid, board_id):
        """
        Returns True if the user specified by netid has access to the board
        specified by board_id, else returns False.
        """
        return len(list(Access.query.filter_by(netid=netid, board_id=board_id))) == 1

    @classmethod
    def get_lists_by_board_id(cls, board_id):
        return list(List.query.filter_by(board_id=board_id))

    @classmethod
    def add_board(cls, name):
        """
        Adds a board. Add a record in Access at the same time.
        """
        try:
            board = Board(name)
            db.session.add(board)
            db.session.flush()
            db.session.refresh(board)   # to let the board has attribute `id`
            access = Access(board.id, g.user.netid)
            db.session.add(access)
            db.session.commit()
            return True
        except:
            db.session.rollback()
            return False
