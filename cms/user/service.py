from cms.extensions import db
from .models import User


class UserService:
    def get_number_of_user(self):
        return db.session.query(User).count()
