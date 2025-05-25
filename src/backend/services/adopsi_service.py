from models import Adopsi
from database import db
from datetime import datetime

def ajukan_adopsi(user_id, kucing_id):
    adopsi = Adopsi(user_id=user_id, kucing_id=kucing_id, tanggal=datetime.utcnow(), status='pending')
    db.session.add(adopsi)
    db.session.commit()
    return adopsi

def ubah_status_adopsi(adopsi_id, status_baru):
    adopsi = Adopsi.query.get(adopsi_id)
    if adopsi:
        adopsi.status = status_baru
        db.session.commit()
    return adopsi

def get_adopsi_user(user_id):
    return Adopsi.query.filter_by(user_id=user_id).all()
