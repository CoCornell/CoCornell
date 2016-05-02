import uuid
import base64
from threading import Thread

from flask import request, g
from flask.ext.login import login_required

from mysite import app, ALLOWED_EXTENSIONS
from mysite.models.list import List
from mysite.models.card import Card
from mysite.models.ocr import OCR
from mysite.ocr.ocr import ocr
from mysite.api.const import Error
from mysite.api.utils import ok, error


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
    Upload an image to a list,
    return JSON.
    """
    list_id = request.form.get("list_id")
    base64_str = request.form.get("file")

    if not list_id:
        return error(Error.EMPTY_LIST_ID, 400)
    if not base64_str:
        return error(Error.EMPTY_IMAGE, 400)
    if not List.has_access_to(g.user.netid, list_id):
        return error(Error.NO_ACCESS_TO_LIST, 400)

    decoded = base64.decodestring(base64_str)
    filename = str(uuid.uuid4()) + ".png"
    image_path = app.config['IMAGE_PATH'] + filename
    with open(image_path, "wb") as f:
        f.write(decoded)

    card = Card.add_card(list_id, filename, True)

    image_path = app.config['IMAGE_PATH'] + filename
    thread = Thread(target=async_ocr, args=[app, image_path, card.id])
    thread.start()

    return ok({"created": True, "card": card.to_dict()})
