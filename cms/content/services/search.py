from cms.extensions import db
from cms.content.models import Article


class SearchContentService:
    def search_content(self, keyword, offset=0, limit=10):
        return (
            db.session.query(Article)
            .filter(Article.markdown_content.like(f"%{keyword}%"))
            .offset(offset)
            .limit(limit)
        )
