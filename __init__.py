from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager


app = Flask(__name__, static_url_path='/static')

app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'secret_key'
app.config['SQLALCHEMY_ECHO'] = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://%s:%s@%s/%s" % ("yhf", "123", "localhost:3306", "cocornell")
app.config['JSON_AS_ASCII'] = False


db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
