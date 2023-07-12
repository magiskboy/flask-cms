from flask_admin import Admin, expose, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_adminlte3 import AdminLTE3


class BaseModelView(ModelView):
    list_template = 'flask-admin/model/list.html'
    create_template = 'flask-admin/model/create.html'
    edit_template = 'flask-admin/model/edit.html'
    details_template = 'flask-admin/model/details.html'

    create_modal_template = 'flask-admin/model/modals/create.html'
    edit_modal_template = 'flask-admin/model/modals/edit.html'
    details_modal_template = 'flask-admin/model/modals/details.html'

    can_export = True

    column_display_pk = ("id_",)
    column_hide_backrefs = False
    column_exclude_list = ("id_",)


class IndexView(AdminIndexView):
    @expose("/", methods=["GET"])
    def index(self):
        from cms.user.service import UserService
        from cms.content.services.content import ContentService

        user_service = UserService()
        content_service = ContentService()

        overview = {
            "access": 11_453,
            "users": user_service.get_number_of_user(),
            "articles": content_service.get_number_of_articles(),
            "categories": content_service.get_number_of_categories(),
        }
        return self.render("admin/index.html", overview=overview)


admin = Admin(
    name="Flask CMS Admin",
    template_mode="bootstrap4",
    index_view=IndexView(),
    base_template="admin/base.html",
)


def load_blueprint_app(app):
    admin.init_app(app)
    AdminLTE3(app)
