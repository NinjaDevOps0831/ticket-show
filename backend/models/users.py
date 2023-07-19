from werkzeug.security import check_password_hash, generate_password_hash

from extensions import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    password_hash = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, username, is_admin, password, email):
        self.username = username
        self.is_admin = is_admin
        self.password_hash = generate_password_hash(password)
        self.email = email

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)