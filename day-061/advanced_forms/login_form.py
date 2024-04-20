from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class LoginForm(FlaskForm):
    username = StringField(label='Username', validators=[
        DataRequired(message="This field is required."),
        Email(message="Invalid email address.")])

    password = PasswordField(label='Password', validators=[
        DataRequired(message="This field is required."),
        Length(min=8, message="Password must be at least 8 characters long.")])

    submit = SubmitField(label='Login')
