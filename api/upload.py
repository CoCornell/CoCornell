from threading import Thread
import os

from flask import request
from werkzeug import secure_filename

from mysite import app
from mysite.views.upload import allowed_file, async_ocr
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
    """
    list_id = request.form.get("list_id")
    f = request.files['file']

    if not list_id:
        return error(Error.EMPTY_LIST_ID, 400)
    if not f:
        return error(Error.EMPTY_IMAGE, 400)

    if f and allowed_file(f.filename):
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        card = Card.add_card(list_id, f.filename, True)

        image_path = app.config['IMAGE_PATH'] + filename
        thread = Thread(target=async_ocr, args=[app, image_path, card.id])
        thread.start()

        return ok({"created": True, "card": card.to_dict()})
