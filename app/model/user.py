from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=False, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    level = db.Column(db.BigInteger, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

    def set_password(self, password):
        # Method to hash the password
        self.password = generate_password_hash(password)

    def check_password(self, password):
        # Method to check hashed password
        return check_password_hash(self.password, password)
    

