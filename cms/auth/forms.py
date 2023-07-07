from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField
from wtforms.validators import Regexp, DataRequired


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Regexp(r"^[\w\d\_\-]{8,20}$")])
    password = PasswordField("Password", validators=[DataRequired(), Regexp(r"^[\w\d\_]{8,20}$")])
