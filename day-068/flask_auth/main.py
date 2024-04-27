from os import urandom
from flask import Flask, render_template, request, url_for, redirect, flash, \
    send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, \
    current_user, logout_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired, URL, Email, Length

app = Flask(__name__)
app.config['SECRET_KEY'] = urandom(32)


class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)


class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    username: Mapped[str] = mapped_column(String(100))


with app.app_context():
    db.create_all()


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


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    new_user = User()
    form = RegisterUserForm()
    if form.validate_on_submit():
        form.populate_obj(new_user)
        existing_user = db.session.execute(
            db.select(User).where(User.email == new_user.email)).scalar()
        if existing_user:
            flash("Email already registered, log in instead.")
            return redirect(url_for('login'))

        new_user.password = generate_password_hash(
            new_user.password, method="scrypt:32768:8:1", salt_length=16)
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)

        return redirect(url_for('secrets'))

    return render_template("register.html", form=form)


@app.route('/login', methods=["GET", "POST"])
def login():
    login_data = User()
    form = LoginUserForm()
    if form.validate_on_submit():
        form.populate_obj(login_data)
        user = db.session.execute(
            db.select(User).where(User.email == login_data.email)).scalar()

        if not user:
            flash("No user found with matching email.")
        elif not check_password_hash(user.password, login_data.password):
            flash('Password incorrect, please try again.')
        else:
            login_user(user)

            return redirect(url_for('secrets'))

    return render_template("login.html", form=form)


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html")


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    return send_from_directory('static', "files/cheat_sheet.pdf")


if __name__ == "__main__":
    app.run(debug=True)
