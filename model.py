import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate




app = Flask(__name__)
app.config['SECRET_KEY'] = "Password"

# database
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)


class Joke(db.Model):
    __tablename__ = 'jokes'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String)
    icon_url = db.Column(db.String)
    value = db.Column(db.Text)

    def __init__(self, url, icon_url, value):
        self.url = url
        self.icon_url = icon_url
        self.value = value

        def __repr__(self):
            return f"random joke: {value}"


