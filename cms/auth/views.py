from flask import Blueprint, render_template, flash, redirect, url_for
from flask.views import MethodView
from flask_login import login_user
from cms.user.service import UserService
from .forms import LoginForm


class LoginView(MethodView):
    def __init__(self, user_service):
        self.user_service = user_service

    def get(self):
        form = LoginForm()
        return render_template("auth/login.html", form=form)

    def post(self):
        form = LoginForm()
        form.validate_on_submit()
        if form.errors:
            for error in form.errors:
                flash(str(error), "error")
            return redirect(url_for("auth.login"))
        
        user = self.user_service.get_user_by_username(form.username.data)
        if not (user and user.verify_password(form.password.data)):
            flash("Credentials is wrong", "info")
            return redirect(url_for("auth.login"))

        login_user(user)
        return redirect(url_for("feed.index"))


def load_blueprint_app(app):
    bp = Blueprint("auth", __name__)

    user_service = UserService()

    bp.add_url_rule("/login", view_func=LoginView.as_view("login", user_service))

    app.register_blueprint(bp, url_prefix="/auth")
