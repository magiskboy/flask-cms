import os


def _get_app_env(name, fallback = None, prefix = "CMS_"):
    return os.getenv(prefix + name, fallback)


class BaseSetting:
    APP_NAME = _get_app_env("APP_NAME", "Flask CMS")
    DB_HOST = _get_app_env("DB_HOST", "localhost")
    DB_PORT = _get_app_env("DB_PORT", "3306")
    DB_NAME = _get_app_env("DB_NAME", "flask_cms")
    DB_USER = _get_app_env("DB_USER", "flask_cms")
    DB_PASS = _get_app_env("DB_PASS", "flask_cms")

    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

    ADMIN_SIDEBAR = [
        {
            "title": "Overview",
            "items": [{"title": "Dashboard", "link": "/admin"}],
        },
        {
            "title": "Post",
            "items": [
                {"title": "List", "link": "#"},
                {"title": "Pending post", "link": "#"},
                {"title": "Deleted post", "link": "#"},
            ],
        },
        {
            "title": "User",
            "items": [
                {"title": "Active user", "link": "/admin/users"},
                {"title": "Deleted user", "link": "/admin/users?inactive=true"},
            ],
        },
        {
            "title": "Category",
            "items": [
                {"title": "List", "link": ""},
                {"title": "Deleted category", "link": ""},
            ],
        },
    ]


class DevelopmentSetting(BaseSetting):
    TEMPLATES_AUTO_RELOAD = True


def get_setting(name):
    return {
        "development": DevelopmentSetting,
    }.get(name, DevelopmentSetting)
