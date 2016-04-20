from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager

import os


app = Flask(__name__, static_url_path='/static')


IMAGE_PATH = os.path.dirname(os.path.abspath(__file__)) + "/static/uploads/"
UPLOAD_FOLDER = IMAGE_PATH
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'secret_key'
app.config['SQLALCHEMY_ECHO'] = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://%s:%s@%s/%s" % ("yhf", "123", "localhost:3306", "cocornell")
app.config['JSON_AS_ASCII'] = False
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['IMAGE_PATH'] = IMAGE_PATH


db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

from mysite.api import api
app.register_blueprint(api, url_prefix="/api")
