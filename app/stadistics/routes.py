from datetime import datetime
from . import stadistic
from app import db

from ./models import sendRegister
db.create_all

def saveRegister(method):
    try:
        num = sendRegister.query.filter_by(method=method).all()
        num = num + 1
        sends = sendRegister(sends = num, last_send = datetime.now().date())
        db.session.add(sends)
        db.session.commit()
        return True
    except Exception as e:
        return False
