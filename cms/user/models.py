from enum import Enum
from werkzeug.security import check_password_hash, generate_password_hash
from markupsafe import Markup
from cms.admin import BaseModelView
from cms.extensions import db
from cms.utils import database


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
    def get_by_username(cls, username):
        return db.session.query(cls).filter(User.username==username).first()

    def __str__(self):
        return self.fullname


class UserModelView(BaseModelView):
    column_filters = ("role",)
    column_list = ("id_", "profile_url", "fullname", "email", "role")
    column_searchable_list = ['fullname', 'username', 'email']
    column_editable_list = ('role',)

    def _display_thumbnail(view, context, model, name):
        return Markup(
            '<center><img src="{}" class="rounded img-thumbnail mx-auto" width="48" height="48" /></center>' \
            .format(model.profile_url)
        )

    column_formatters = {
        "profile_url": _display_thumbnail,
    }


