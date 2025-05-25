from database import db
from models import Perawatan
from datetime import date

# Buat perawatan baru
def tambah_perawatan(user_id, cat_name, jenis_perawatan, tanggal=None):
    if tanggal is None:
        tanggal = date.today()
    perawatan = Perawatan(
        user_id=user_id,
        cat_name=cat_name,
        jenis_perawatan=jenis_perawatan,
        tanggal=tanggal
    )
    db.session.add(perawatan)
    db.session.commit()
    return perawatan

# Ambil semua perawatan milik user tertentu
def get_perawatan_by_user(user_id):
    return Perawatan.query.filter_by(user_id=user_id).all()

# Update status perawatan
def update_status_perawatan(perawatan_id, status_baru):
    perawatan = Perawatan.query.get(perawatan_id)
    if perawatan:
        perawatan.status = status_baru
        db.session.commit()
    return perawatan

# Hapus perawatan
def hapus_perawatan(perawatan_id):
    perawatan = Perawatan.query.get(perawatan_id)
    if perawatan:
        db.session.delete(perawatan)
        db.session.commit()
    return perawatan
