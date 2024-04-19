from flask import Flask, render_template, redirect, request
from markupsafe import escape
from requests import get
from datetime import datetime
from post import Post

from mailer import receive_mail

app = Flask(__name__)


def get_posts():
    data_url = "https://api.npoint.io/674f5423f73deab1e9a7"
    r = get(data_url)
    blog_data = r.json()
    posts = []
    for p in blog_data:
        p = Post(
            p["id"],
            p["title"],
            p["subtitle"],
            p["body"],
            "Admin",
            datetime.now().date(),
            p["image_url"])
        posts.append(p)

    return posts


@app.route("/css")
def css():
    return redirect(f"/static/css/styles.css")


@app.route("/js/<path:path>")
def js(path):
    return redirect(f"/static/js/{escape(path)}")


@app.route("/assets/<path:path>")
def assets(path):
    return redirect(f"/static/assets/{escape(path)}")


@app.route('/')
def home():
    posts = get_posts()
    return render_template("index.html", posts=posts)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "GET":
        return render_template("contact.html", sent=False)

    data = request.form
    receive_mail(
        f"Contact form email from: {data["name"]} at {data["email"]}",
        data["message"])
    return render_template("contact.html", sent=True)


@app.route('/post_example')
def post_example():
    return render_template("post_example.html")


@app.route("/posts/<int:index>")
def get_post(index):
    posts = get_posts()
    requested_post = None
    for blog_post in posts:
        if blog_post.id == index:
            requested_post = blog_post

    return render_template("blog_post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
