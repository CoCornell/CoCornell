from mysite import db
from mysite.models import SerializableModel


class OCR(db.Model, SerializableModel):

    __tablename__ = 'ocr'

    id = db.Column(db.Integer, primary_key=True)
    card_id = db.Column(db.Integer)
    text = db.Column(db.Text)

    def __init__(self, card_id, text):
        self.card_id = card_id
        self.text = text

    def __repr__(self):
        return '<OCR [%d], %s>' % (self.card_id, self.text)

    @classmethod
    def add_ocr(cls, card_id, text):
        """
        Adds an OCR relationship.
        """
        ocr_relation = OCR(card_id, text)
        db.session.add(ocr_relation)
        db.session.commit()
        return ocr_relation
