from .extensions import db 

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))

class Stage(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    current_stage = db.Column(db.String(20))