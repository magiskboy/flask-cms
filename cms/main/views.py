from flask import Blueprint, render_template, request
from flask.views import MethodView
from cms.content.services.feed import FeedService
from cms.content.services.category import CategoryService


class HomepageView(MethodView):
    def __init__(self, feed_service, category_service):
        self.feed_service = feed_service
        self.category_service = category_service

    def get(self):
        page = request.args.get("page", type=int) or 10
        highlight_article = self.feed_service.get_highlight_article()
        categories = self.category_service.get_categories(offset=0, limit=8)
        articles = self.feed_service.get_list_articles(offset=page * 10, limit=10)

        return render_template(
            "main/index.html",
            highlight_article=highlight_article,
            articles=articles,
            categories=categories,
        )


def load_blueprint_app(app):
    bp = Blueprint("main", __name__)

    feed_service = FeedService()
    category_service = CategoryService()

    bp.add_url_rule(
        "/", view_func=HomepageView.as_view("homepage", feed_service, category_service)
    )

    app.register_blueprint(bp, url_prefix="/")
