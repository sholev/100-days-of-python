from os import urandom
from flask import Flask, render_template, redirect, request, url_for
from flask_bootstrap import Bootstrap5
from book_form import AddBookForm, EditBookForm
from books_db import BooksDB

app = Flask(__name__)
app.secret_key = urandom(32)
Bootstrap5(app)
db = BooksDB(app)


@app.route('/')
def home():
    all_books = db.get_all()

    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddBookForm()
    if form.validate_on_submit():
        db.add(
            title=form.title.data,
            author=form.author.data,
            rating=form.rating.data)

        return redirect(url_for("home"))

    return render_template("add.html", form=form)


@app.route("/edit/<int:book_id>", methods=["GET", "POST"])
def edit(book_id):
    book = db.get_by_id(book_id)
    form = EditBookForm(obj=book)
    if form.validate_on_submit():
        db.update(
            book_id,
            title=form.title.data,
            author=form.author.data,
            rating=form.rating.data)

        return redirect(url_for("home"))

    return render_template("edit.html", form=form, book=book)


@app.route("/delete/<int:book_id>", methods=["GET", "POST"])
def delete(book_id):
    book = db.get_by_id(book_id)
    if request.method == "POST":
        db.delete(book_id)

        return redirect(url_for("home"))

    return render_template("delete.html", book=book)


if __name__ == "__main__":
    app.run(debug=True)
