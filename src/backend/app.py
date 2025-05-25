# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from models import Cat

app = Flask(__name__)

# Contoh: SQLite (lokal)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meowphoria.db'

# Kalau pakai MySQL atau PostgreSQL:
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@localhost/db_name'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/db_name'

db = SQLAlchemy(app)

# Import models agar terdaftar
from models import Cat

# Buat database pertama kali
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)

