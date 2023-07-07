from flask import Blueprint
from flask.views import MethodView


class HomepageView(MethodView):
    def get(self):
        return "Hello, world"


def load_blueprint_app(app):
    bp = Blueprint("main", __name__)

    bp.add_url_rule("/", view_func=HomepageView.as_view("homepage"))

    app.register_blueprint(bp, url_prefix="/")
