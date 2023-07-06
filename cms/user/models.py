from enum import Enum
from werkzeug.security import check_password_hash, generate_password_hash
from ..extensions import db
from ..utils import database


class UserRole(str, Enum):
    writer = "writer"
    normal = "normal"
    anonymous = "anonymous"
    admin = "admin"


class User(database.Model, db.Model):
    fullname = db.Column(db.String(50), nullable=False)
    profile_url = db.Column(db.String(200), nullable=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    hash_password = db.Column(db.String(128), nullable=False)
    role = db.Column(db.Enum(UserRole), default=UserRole.normal)
    email = db.Column(db.String(200), nullable=True)

    @property
    def password(self):
        raise RuntimeError("Set value is denided!!!")

    @password.setter
    def password(self, password):
        self.hash_password = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.hash_password, password)

    @classmethod
    def update_by_username(cls, username, data):
        db.session.query(cls).filter(username=username).update(data)

    @classmethod
    def delete_by_username(cls, username, is_soft = True):
        query = db.session.query(cls).filter(username=username)
        if is_soft:
            query.update({"is_deleted": True})
        else:
            query.delete()
    
    @classmethod
    def get_by_username(cls, username):
        return db.session.query(cls).filter(User.username==username).first()

    def __str__(self):
        return f"<User {self.id_}: {self.username}>"
