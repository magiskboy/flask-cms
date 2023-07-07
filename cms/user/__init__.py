from cms.admin import register_model_view
from .models import User, UserModelView


def register_module():
    register_model_view(User, UserModelView)
