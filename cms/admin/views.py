from flask.views import MethodView
from flask import render_template, Blueprint


class User(MethodView):
    def get(self):
        return render_template("admin/index.html")


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
    
    bp.add_url_rule("", view_func=User.as_view("admin"))

    app.register_blueprint(bp, url_prefix="/admin")
