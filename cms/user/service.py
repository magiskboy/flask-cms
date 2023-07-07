from cms.extensions import db
from .models import User


class UserService:
    def get_number_of_user(self):
        return db.session.query(User).count()

    def get_user_by_username(username):
        return db.session.query(User).filter(
            User.username==username,
        ).first()
