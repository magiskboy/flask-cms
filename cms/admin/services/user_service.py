import logging
from cms.user.models import User


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

    def get_list_user(self, filters=None, offset = 0):
        return User.get_list(filters, ("id_", "fullname", "profile_url", "role"), offset)

    def get_user(self, id_or_username):
        if isinstance(id_or_username, int):
            return User.get(id_or_username)

        elif isinstance(id_or_username, str):
            return User.get_by_username(id_or_username)

        else:
            raise TypeError(f"id_or_username must be str or int, not {type(id_or_username)}")
