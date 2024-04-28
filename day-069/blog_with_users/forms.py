from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField
from wtforms.validators import DataRequired, URL, Email, Length
from flask_ckeditor import CKEditorField


password_validators = [DataRequired(), Length(min=8, max=100)]
email_validators = [DataRequired(), Email(), Length(max=100)]
username_validators = [DataRequired(), Length(min=3, max=100)]


class RegisterUserForm(FlaskForm):
    email = EmailField("Email", email_validators)
    password = PasswordField("Password", password_validators)
    username = StringField("Username", username_validators)
    submit = SubmitField("Sign me up.")


class LoginUserForm(FlaskForm):
    email = EmailField("Email", email_validators)
    password = PasswordField("Password", password_validators)
    submit = SubmitField("Let me in.")


class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


class CommentForm(FlaskForm):
    text = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("Submit Comment")
