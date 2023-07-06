from flask.views import MethodView
from flask import render_template, Blueprint, request
from werkzeug.exceptions import NotFound
from .services.user_service import UserService


class DashboardView(MethodView):
    def get(self):
        return render_template("admin/index.html")


class ListUserView(MethodView):
    def __init__(self, user_service):
        self.user_service = user_service

    def get(self):
        offset = request.args.get("page", "0", type=int)
        limit = request.args.get("per_page", 10, type=int)
        keyword = request.args.get("keyword")
        inactive = request.args.get("inactive")

        users = self.user_service.get_list_user(keyword, inactive, offset, limit)

        return render_template("admin/list-user.html", users=users)


class DetailUserView(MethodView):
    def __init__(self, user_service):
        self.user_service = user_service

    def get(self, username):
        user = self.user_service.get_user(username)

        if not user:
            NotFound()
        return render_template("admin/detail-user.html", user=user)


def load_blueprint_app(app):
    bp = Blueprint("admin", __name__)

    @bp.errorhandler(404)
    def handle_404(e):
        return render_template("admin/404.html")

    @bp.errorhandler(401)
    def handle_401(e):
        return render_template("admin/401.html")

    @bp.errorhandler(500)
    def handle_500(e):
        return render_template("admin/500.html")
    
    user_service = UserService()

    bp.add_url_rule("/users", view_func=ListUserView.as_view("users", user_service))
    bp.add_url_rule("/users/<username>", view_func=DetailUserView.as_view("detail_user", user_service))
    bp.add_url_rule("/", view_func=DashboardView.as_view("dashboard"))

    app.register_blueprint(bp, url_prefix="/admin")
