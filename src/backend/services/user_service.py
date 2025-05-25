from models import User
from database import db

def register_user(nama, email, password, is_admin=False):
    user = User(nama=nama, email=email, password=password, is_admin=is_admin)
    db.session.add(user)
    db.session.commit()
    return user

def get_user_by_email(email):
    return User.query.filter_by(email=email).first()

def get_user_by_id(user_id):
    return User.query.get(user_id)
