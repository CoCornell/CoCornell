from mysite import db
from mysite.models import SerializableModel
from mysite.models.ocr import OCR


class Card(db.Model, SerializableModel):

    __tablename__ = 'card'

    id = db.Column(db.Integer, primary_key=True)
    list_id = db.Column(db.Integer)
    content = db.Column(db.String)
    is_image = db.Column(db.BOOLEAN)

    def __init__(self, list_id, content, is_image=False):
        self.list_id = int(list_id)
        self.content = content
        self.is_image = is_image

    def __repr__(self):
        return '<Card [%d]>' % self.id

    @classmethod
    def get_card_by_id(cls, card_id):
        return Card.query.filter_by(id=card_id).first()

    @classmethod
    def add_card(cls, list_id, content, is_image=False):
        """
        Adds a card to the list, and returns the card.
        """
        new_card = Card(list_id, content, is_image)
        db.session.add(new_card)
        db.session.flush()
        db.session.refresh(new_card)  # to let the new_card has attribute `id`
        db.session.commit()
        return new_card

    @classmethod
    def delete_card_by_id(cls, card_id):
        cards = db.session.query(Card).filter(Card.id == card_id)
        for card in cards:
            if card.is_image:
                OCR.delete_ocr_by_card_id(card.id)
        cards.delete()
        db.session.commit()
