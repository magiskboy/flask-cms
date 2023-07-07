from cms.admin import register_model_view
from .models import UserModelView, User


def load_blueprint_app(app):
    register_model_view(User, UserModelView)
