import uuid
import base64
from threading import Thread

from flask import request

from mysite import app
from mysite.views.upload import async_ocr
from mysite.models.card import Card
from mysite.api import api
from mysite.api.token import auth
from mysite.api.const import Error
from mysite.api.utils import ok, error


@api.route("/upload/", methods=['POST'])
@auth.login_required
def upload_image():
    """
    Upload an image to a list.
    The image should be base64 encoded.
    """
    list_id = request.form.get("list_id")
    base64_str = request.form.get("file")

    if not list_id:
        return error(Error.EMPTY_LIST_ID, 400)
    if not base64_str:
        return error(Error.EMPTY_IMAGE, 400)

    decoded = base64.b64decode(base64_str)
    filename = str(uuid.uuid4()) + ".png"
    image_path = app.config['IMAGE_PATH'] + filename
    with open(image_path, "wb") as f:
        f.write(decoded)

    card = Card.add_card(list_id, filename, True)

    image_path = app.config['IMAGE_PATH'] + filename
    thread = Thread(target=async_ocr, args=[app, image_path, card.id])
    thread.start()

    return ok({"created": True, "card": card.to_dict()})
