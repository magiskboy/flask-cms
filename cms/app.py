from flask import Flask
from .extensions import configure_sqlalchemy, configure_template
from .setting import get_setting
from cms.admin.views import load_blueprint_app as register_admin_blueprint
from cms.user.views import load_blueprint_app as register_user_blueprint
from cms.content.views import load_blueprint_app as register_content_blueprint


def create_app(config_name=None):
    app = Flask(__name__, template_folder="templates")
    app.url_map.strict_slashes = False
    app.config.from_object(get_setting(config_name))
    
    # load extensions
    configure_template(app)
    configure_sqlalchemy(app)
    # configure_login_manager(app)

    # load modules
    register_admin_blueprint(app)
    register_user_blueprint(app)
    register_content_blueprint(app)
    
    return app
