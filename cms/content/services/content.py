from cms.extensions import db
from .models import Article, Category


class ContentService:
    def get_number_of_articles(self):
        return db.session.query(Article).count()

    def get_number_of_categories(self):
        return db.session.query(Category).count()
