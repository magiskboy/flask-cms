from cms.extensions import db
from cms.content.models import Article


class FeedService:
    def get_highlight_article(self):
        return db.session.query(Article).order_by(Article.id_).first()

    def get_list_articles(self, offset=0, limit=10):
        return db.session.query(Article).order_by(Article.id_).offset(offset).limit(limit)
