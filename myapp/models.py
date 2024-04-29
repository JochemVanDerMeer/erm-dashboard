from .extensions import db 

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))

class RowStage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stage_number = db.Column(db.String(50))
    start = db.Column(db.String(50))
    finish = db.Column(db.String(50))
    distance = db.Column(db.String(50))
    cox = db.Column(db.String(50))
    bow = db.Column(db.String(50))
    stroke = db.Column(db.String(50))
    next_cox = db.Column(db.String(50))
    next_bow = db.Column(db.String(50))
    next_stroke = db.Column(db.String(50))