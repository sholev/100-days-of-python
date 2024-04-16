from flask import Flask, render_template
from datetime import datetime
from requests import get
from random import randint
from post import Post

app = Flask(__name__)


def get_posts():
    data_url = "https://api.npoint.io/c790b4d5cab58020d391"
    r = get(data_url)
    blog_data = r.json()
    posts = []
    for p in blog_data:
        post = Post(p["id"], p["title"], p["subtitle"], p["body"])
        posts.append(post)

    return posts


def get_footer():
    return f"Copyright {datetime.now().year}. Built by Asen"


@app.route('/')
def home():
    random_number = randint(1, 10)

    return render_template(
        "index.html",
        num=random_number,
        footer=get_footer())


@app.route('/blog/')
def get_blog():
    posts = get_posts()

    return render_template(
        "blog.html",
        blog_data=posts,
        footer=get_footer())


@app.route("/post/<int:index>")
def get_post(index):
    posts = get_posts()
    requested_post = None
    for blog_post in posts:
        if blog_post.id == index:
            requested_post = blog_post

    return render_template(
        "blog_post.html",
        post=requested_post,
        footer=get_footer())


@app.route('/guess/<name>')
def guess(name):
    name_data = get(f"https://api.agify.io?name={name}").json()
    gender_data = get(f"https://api.genderize.io?name={name}").json()

    return render_template(
        "guess.html",
        name=name,
        age=name_data["age"],
        gender=gender_data["gender"])


if __name__ == "__main__":
    app.run(debug=True)
