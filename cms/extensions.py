from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


db = SQLAlchemy()
migrate = Migrate()

def configure_sqlalchemy(app):
    db.init_app(app)
    migrate.init_app(app, db)


login_manager = LoginManager()

def configure_login_manager(app):
    login_manager.init_app(app)


def configure_template(app):
    @app.context_processor
    def inject_context():
        return {
            "admin_sidebar": app.config.get("ADMIN_SIDEBAR"),
            "admin_name": app.config.get("APP_NAME"),
            "enumerate": enumerate,
        }
