from os import urandom
from hashlib import md5
from datetime import date
from flask import (Flask, abort, render_template, redirect, url_for, flash,
                   request, Response)
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_login import (login_user, LoginManager, current_user, logout_user,
                         login_required)
from flask_sqlalchemy import SQLAlchemy
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash

from models import Base, User, BlogPost, Comment
from forms import CreatePostForm, RegisterUserForm, LoginUserForm, CommentForm

app = Flask(__name__)
app.config['SECRET_KEY'] = urandom(32)
ckeditor = CKEditor(app)
Bootstrap5(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

with app.app_context():
    db.create_all()

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)


@app.route('/static/css/styles.css')
def css():
    css_path = '../../day-059/bootstrap_blog/static/css/styles.css'
    with open(css_path, mode='rt', encoding='utf8') as file:
        text = file.read()

        return Response(text, mimetype='text/css')


@app.route('/static/js/scripts.js')
def js():
    scripts_path = '../../day-059/bootstrap_blog/static/js/scripts.js'
    with open(scripts_path, mode='rt', encoding='utf8') as file:
        text = file.read()

        return Response(text, mimetype='text/plain')


def avatar(email, size=100, rating='g', default='retro', force_default=False):
    hash_value = md5(email.lower().encode('utf-8')).hexdigest()
    params = f"{hash_value}?s={size}&d={default}&r={rating}&f={force_default}"

    return f"https://www.gravatar.com/avatar/{params}"


def admin_only(func):
    @wraps(func)
    @login_required
    def wrapper(*args, **kwargs):
        if current_user.id != 1:
            return abort(403)
        return func(*args, **kwargs)

    return wrapper


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

        return redirect(url_for('home'))

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

            return redirect(url_for('home'))

    return render_template("login.html", form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/')
def home():
    result = db.session.execute(db.select(BlogPost))
    posts = result.scalars().all()
    return render_template("index.html", all_posts=posts)


@app.route('/post/<int:post_id>', methods=["GET", "POST"])
def show_post(post_id):
    requested_post = db.get_or_404(BlogPost, post_id)
    comment_form = CommentForm()
    if comment_form.validate_on_submit():
        if not current_user.is_authenticated:
            flash("You need to login or register to comment.")
            return redirect(url_for("login"))

        new_comment = Comment()
        comment_form.populate_obj(new_comment)
        new_comment.author = current_user
        new_comment.post = requested_post
        db.session.add(new_comment)
        db.session.commit()

    return render_template('post.html', post=requested_post, form=comment_form,
                           get_avatar=avatar)


@app.route('/new-post', methods=['GET', 'POST'])
@admin_only
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost()
        form.populate_obj(new_post)
        new_post.author = current_user
        new_post.date = date.today().strftime('%B %d, %Y')
        db.session.add(new_post)
        db.session.commit()

        return redirect(url_for('home'))

    return render_template('make-post.html', form=form)


@app.route('/edit-post/<int:post_id>', methods=['GET', 'POST'])
@admin_only
def edit_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    edit_form = CreatePostForm(obj=post)
    if edit_form.validate_on_submit():
        edit_form.populate_obj(post)
        db.session.commit()

        return redirect(url_for('show_post', post_id=post.id))

    return render_template('make-post.html', form=edit_form, is_edit=True)


@app.route('/delete/<int:post_id>', methods=['POST'])
@admin_only
def delete_post(post_id):
    if request.method == "POST":
        post_to_delete = db.get_or_404(BlogPost, post_id)
        db.session.delete(post_to_delete)
        db.session.commit()

    return redirect(url_for('home'))


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
