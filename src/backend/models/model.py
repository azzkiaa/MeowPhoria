from database import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)  # Simpan dalam bentuk hashed
    is_admin = db.Column(db.Boolean, default=False)

    adopsi = db.relationship('Adopsi', backref='user', lazy=True)
    perawatan = db.relationship('Perawatan', backref='user', lazy=True)
    hasil_kuesioner = db.relationship('HasilKuesioner', backref='user', lazy=True)


class Cat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer)
    breed = db.Column(db.String(100))
    sex = db.Column(db.String(100))
    dificulty = db.Column(db.String(100))
    deskripsi = db.Column(db.Text)
    tersedia = db.Column(db.Boolean, default=True)

    adopsi = db.relationship('Adopsi', backref='kucing', lazy=True)


class Adopsi(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    kucing_id = db.Column(db.Integer, db.ForeignKey('kucing.id'), nullable=False)
    tanggal = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(50), default='pending')  # pending, approved, rejected


class LayananPerawatan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100), nullable=False)
    harga = db.Column(db.Integer)
    deskripsi = db.Column(db.Text)


class Perawatan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    layanan_id = db.Column(db.Integer, db.ForeignKey('layanan_perawatan.id'), nullable=False)
    tanggal = db.Column(db.DateTime, default=datetime.utcnow)

    layanan = db.relationship('LayananPerawatan')


class HasilKuesioner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    hasil_rekomendasi = db.Column(db.String(100))
    tanggal = db.Column(db.DateTime, default=datetime.utcnow)
