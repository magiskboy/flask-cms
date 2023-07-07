from cms.admin import register_model_view
from .models import Article, Category, ArticalModelView, Tag, Comment, TagModelView


def load_blueprint_app(app):
    register_model_view(Article, ArticalModelView)
    register_model_view(Category)
    register_model_view(Tag, TagModelView)
    register_model_view(Comment)
