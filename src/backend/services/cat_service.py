from models import Cat
from database import db

def list_kucing_tersedia():
    return Cat.query.filter_by(tersedia=True).all()

def tambah_kucing(name, age, breed, sex, dificulty, deskripsi):
    kucing = Cat(name=name, age=age, breed=breed, sex=sex, dificulty=dificulty, deskripsi=deskripsi, tersedia=True)
    db.session.add(kucing)
    db.session.commit()
    return kucing

def ubah_ketersediaan_kucing(kucing_id, tersedia):
    kucing = Cat.query.get(kucing_id)
    if kucing:
        kucing.tersedia = tersedia
        db.session.commit()
    return kucing
