import logging
from cms.user.models import User
from cms.extensions import db


logger = logging.getLogger(__name__)


class UserService:
    def create_new_user(data):
        User.create(data)

    def update_user(id_or_username, data):
        logger.debug(f"update_user({id_or_username})")

        if isinstance(id_or_username, int):
            User.update_by_id(id_or_username)

        elif isinstance(id_or_username, str):
            User.update_by_username(id_or_username, data)

        else:
            raise TypeError(f"id_or_username must be str or int, not {type(id_or_username)}")

    def delete_user(id_or_username):
        logging.debug(f"delete_user({id_or_username})")

        if isinstance(id_or_username, int):
            User.delete_by_id(id_or_username)

        elif isinstance(id_or_username, str):
            User.delete_by_username(id_or_username)

        else:
            raise TypeError(f"id_or_username must be str or int, not {type(id_or_username)}")

    def get_list_user(self, keyword=None, inactive=None, offset = 0, limit = 10):
        query = db.session.query(User)

        if keyword:
            query = query.filter(db.or_(
                User.username.like(f"%{keyword}%"),
                User.email.like(f"%{keyword}%"), 
                User.fullname.like(f"%{keyword}%")
            ))

        query = query.filter(User.is_deleted==(True if inactive == "true" else False))
        query = query.offset(offset).limit(limit)

        return query.all()

    def get_user(self, id_or_username):
        if isinstance(id_or_username, int):
            return User.get(id_or_username)

        elif isinstance(id_or_username, str):
            return User.get_by_username(id_or_username)

        else:
            raise TypeError(f"id_or_username must be str or int, not {type(id_or_username)}")
