from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class CheckList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, index=True, unique=True)
    pickled_list = db.Column(db.Text, nullable=False)