from werkzeug.security import generate_password_hash, check_password_hash
from models import User
from database import db

# Registrasi user baru
def register_user(username, email, password, role='user'):
    if User.query.filter((User.username == username) | (User.email == email)).first():
        return None  # Username/email sudah dipakai
    hashed_pw = generate_password_hash(password)
    user = User(username=username, email=email, password=hashed_pw, role=role)
    db.session.add(user)
    db.session.commit()
    return user

# Verifikasi login
def login_user(username, password):
    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        return user
    return None

# Cek apakah user adalah admin
def is_admin(user):
    return user.role == 'admin'
