from mysite import db
from mysite.models import SerializableModel


class OCR(db.Model, SerializableModel):

    __tablename__ = 'ocr'

    id = db.Column(db.Integer, primary_key=True)
    card_id = db.Column(db.Integer)
    text = db.Column(db.Text)

    def __init__(self, card_id, text):
        self.card_id = card_id
        self.text = text.decode("utf-8").encode("utf-8")

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

    @classmethod
    def get_ocr_by_card_id(cls, card_id):
        return OCR.query.filter_by(card_id=card_id).first()

    @classmethod
    def delete_ocr_by_card_id(cls, card_id):
        db.session.query(OCR).filter(OCR.card_id == card_id).delete()
        db.session.commit()
