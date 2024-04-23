from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea


class MovieFormRate(FlaskForm):
    rating = StringField(
        label="Movie rating (0.0-10):",
        validators=[DataRequired()]
    )
    review = StringField(
        label="Movie review:",
        validators=[DataRequired()],
        widget=TextArea()
    )
    submit = SubmitField("Submit")


class MovieFormAdd(FlaskForm):
    title = StringField(
        label="Movie title:",
        validators=[DataRequired()]
    )
    submit = SubmitField("Search")
