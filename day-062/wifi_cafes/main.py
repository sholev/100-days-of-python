from os import urandom
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
from csv import reader

app = Flask(__name__)
app.config['SECRET_KEY'] = urandom(32)
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField(
        'Cafe name',
        validators=[DataRequired()]
    )
    location = StringField(
        "Cafe Location on Google Maps (URL)",
        validators=[DataRequired(), URL()]
    )
    open = StringField(
        "Opening Time e.g. 08:00",
        validators=[DataRequired()]
    )
    close = StringField(
        "Closing Time e.g. 17:30",
        validators=[DataRequired()]
    )
    coffee_rating = SelectField(
        "☕️Coffee Rating",
        choices=[("☕️" * i, "☕️" * i) for i in range(1, 6)],
        validators=[DataRequired()]
    )
    wifi_rating = SelectField(
        "🛜WiFi Strength Rating",
        choices=[("None", "None")] + [("🛜" * i, "🛜" * i) for i in range(1, 6)],
        validators=[DataRequired()]
    )
    power_rating = SelectField(
        "🔌Power Socket Availability",
        choices=[(item, item) for item in ["Not Available", "Available"]],
        validators=[DataRequired()]
    )
    submit = SubmitField('Submit')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        entry = (
            f"\n{form.cafe.data},"
            f"{form.location.data},"
            f"{form.open.data},"
            f"{form.close.data},"
            f"{form.coffee_rating.data},"
            f"{form.wifi_rating.data},"
            f"{form.power_rating.data}")

        with open("cafe-data.csv", mode="a", encoding='utf-8') as csv_file:
            csv_file.write(entry)
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)

    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
