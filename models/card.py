from mysite import db
from mysite.models import SerializableModel


class Card(db.Model, SerializableModel):

    __tablename__ = 'card'

    id = db.Column(db.Integer, primary_key=True)
    list_id = db.Column(db.Integer)
    content = db.Column(db.String)

    def __init__(self, list_id, content):
        self.list_id = int(list_id)
        self.content = content

    def __repr__(self):
        return '<Card [%d]>' % self.id

    @classmethod
    def add_card(cls, list_id, content):
        """
        Adds a list to the board.
        """
        new_card = Card(list_id, content)
        db.session.add(new_card)
        db.session.commit()
