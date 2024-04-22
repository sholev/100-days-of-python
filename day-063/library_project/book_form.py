from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired


class BookForm(FlaskForm):
    title = StringField(
        label="Book title",
        validators=[DataRequired()])
    author = StringField(
        label="Book author",
        validators=[DataRequired()]
    )
    rating = FloatField(
        label="Book rating",
        validators=[DataRequired()]
    )


class AddBookForm(BookForm):
    submit = SubmitField("Add book")


class EditBookForm(BookForm):
    submit = SubmitField("Edit book")
