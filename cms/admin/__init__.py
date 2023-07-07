from cms.admin.views import BaseModelView
from cms.extensions import db
from .views import admin


def register_model_view(model, model_view=BaseModelView):
    admin.add_view(model_view(model, db.session))
