from cms.extensions import db
from cms.utils.database import Model
from cms.admin import BaseModelView


class Like(Model, db.Model):
    article_id = db.Column(db.Integer(), db.ForeignKey("article.id"), nullable=False)
    user_id = db.Column(db.Integer(), db.ForeignKey("user.id"), nullable=False)
    user = db.relationship("User")


class Comment(Model, db.Model):
    article_id = db.Column(db.Integer(), db.ForeignKey("article.id"), nullable=False)
    user_id = db.Column(db.Integer(), db.ForeignKey("user.id"), nullable=True)
    content = db.Column(db.String(200), nullable=False)
    user = db.relationship("User")


class ArticleTag(db.Model):
    __tablename__ = "article_tag"
    id_ = db.Column("id", db.Integer(), primary_key=True)
    article_id = db.Column(db.Integer(), db.ForeignKey("article.id"), nullable=False)
    tag_id = db.Column(db.Integer(), db.ForeignKey("tag.id"), nullable=False)


class Tag(Model, db.Model):
    name = db.Column(db.String(50), nullable=False, unique=True)
    created_by_id = db.Column(db.Integer(), db.ForeignKey("user.id"), nullable=False)
    created_by = db.relationship("User", backref="created_tags")

    def __str__(self):
        return self.name


class Category(Model, db.Model):
    title = db.Column(db.String(100), nullable=False, unique=True)
    slug = db.Column(db.String(200), nullable=False, unique=True)
    description = db.Column(db.String(500))

    def __str__(self):
        return self.title


class Article(Model, db.Model):
    title = db.Column(db.String(100), nullable=False)
    slug = db.Column(db.String(200), nullable=False, unique=True)
    markdown_content = db.Column(db.Text(), nullable=False)
    summary = db.Column(db.Text(), nullable=False)

    author_id = db.Column(db.Integer(), db.ForeignKey("user.id"), nullable=False)
    author = db.relationship("User", backref="articles")
    
    category_id = db.Column(db.Integer(), db.ForeignKey("category.id"), nullable=False)
    category = db.relationship("Category", backref="articles") 

    like_by = db.relationship("User", secondary="like", backref="liked_articles")

    comments = db.relationship("Comment", backref="article")

    tags = db.relationship("Tag", secondary="article_tag", backref="articles")

    def __str__(self):
        return self.title


class ArticalModelView(BaseModelView):
    column_list = ("title", "category", "summary", "author")
    column_editable_list = ("title", "slug", "markdown_content", "summary", "author", "category", "tags")

class TagModelView(BaseModelView):
    column_list = ("name", "created_by")
    edit_modal = True


class LikeModelView(BaseModelView):
    column_list = ("user", "article")
