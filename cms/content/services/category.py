from cms.extensions import db
from cms.content.models import Category


class CategoryService:
    def get_categories(self, offset = 0, limit = 10):
        return db.session.query(Category).offset(offset).limit(limit)
