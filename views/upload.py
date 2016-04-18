from threading import Thread
import os

from flask import request, redirect
from flask.ext.login import login_required
from werkzeug import secure_filename

from mysite import app, ALLOWED_EXTENSIONS
from mysite.models.list import List
from mysite.models.card import Card
from mysite.models.ocr import OCR
from mysite.ocr.ocr import ocr


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


def async_ocr(app, image_path, card_id):
    with app.app_context():
        text = ocr(image_path)
        OCR.add_ocr(card_id, text)


@app.route("/upload/", methods=['POST'])
@login_required
def upload_image():
    """
    Upload an image to a list.
    """
    list_id = request.form.get("list_id")
    f = request.files['file']
    if f and allowed_file(f.filename):
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        card = Card.add_card(list_id, f.filename, True)

        image_path = app.config['IMAGE_PATH'] + filename
        thread = Thread(target=async_ocr, args=[app, image_path, card.id])
        thread.start()

        return redirect('/board/' + str(List.query.filter_by(id=list_id).first().board_id))
