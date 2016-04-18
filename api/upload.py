from threading import Thread
import os

from flask import request, redirect
from flask.ext.login import login_required

from mysite.models.board import Board
from mysite.models.list import List
from mysite.api import api
from mysite.api.token import auth
from mysite.api.const import Error
from mysite.api.utils import ok, error


@api.route("/upload/", methods=['POST'])
@auth.login_required()
def upload_image():
    """
    Upload an image to a list.
    """
    list_id = request.form.get("list_id")
    f = request.files['file']
    if f and allowed_file(f.filename):
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        card_id = Card.add_card(list_id, f.filename, True)

        image_path = app.config['IMAGE_PATH'] + filename
        thread = Thread(target=async_ocr, args=[app, image_path, card_id])
        thread.start()

        return redirect('/board/' + list_id)
