from . import db

class User(db.Model):
    id = db.Column(db.Integer , primary_key=True)
    name = db.Column(db.String(100) , nullable = False)
    email = db.Column(db.String(50) , nullable=False)
    message = db.Column(db.String(1000) , nullable = False)