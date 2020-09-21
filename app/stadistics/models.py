from app import db
class sendRegister(db.model):
    method = db.Column(db.String, unique=True,nulleable=False)
    sends = db.Column(db.Integer, unique=False,nulleable=False,default=0)
    last_send = db.Column(db.DataTime, unique=False, nulleable=True)
