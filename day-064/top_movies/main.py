from os import urandom
from flask import Flask, render_template, redirect, url_for, request, session
from flask_bootstrap import Bootstrap5
from flask_wtf.csrf import CSRFProtect

from movies_db import MoviesDB
from movie import Movie
from movie_forms import MovieFormRate, MovieFormAdd
from movies_imdb import search

app = Flask(__name__)
app.config['SECRET_KEY'] = urandom(32)
Bootstrap5(app)
csrf = CSRFProtect(app)
db = MoviesDB(app)


@app.route("/")
def home():
    all_movies = db.get_all()
    return render_template("index.html", movies=all_movies)


@app.route("/add", methods=["GET", "POST"])
def add():
    form = MovieFormAdd()
    if form.validate_on_submit():
        title = form.title.data
        session['movies_data'] = search(title)[:10]
        return redirect(url_for("select"))

    return render_template("add.html", form=form)


@app.route("/select", methods=["GET", "POST"])
def select():
    if session.get("movies_data") is None:
        return redirect(url_for("add"))

    movies_data = session.get("movies_data")
    if request.method == "POST":
        index = int(request.args.get("index"))
        movie_data = movies_data[index]
        movie = Movie(
            title=movie_data["title"],
            year=movie_data["year"],
            rating=movie_data["rating"],
            description=movie_data["description"],
            img_url=movie_data["img_url"],
            ranking=movie_data["ranking"],
            review=movie_data["review"],
        )
        db.add(movie)
        db.update_rankings()
        db_movie = db.get_by_title(movie_data["title"])
        session['movies_data'] = None
        return redirect(url_for("rate", movie_id=db_movie.id))

    return render_template("select.html", movies_data=movies_data)


@app.route("/rate/<int:movie_id>", methods=["GET", "POST"])
def rate(movie_id: int):
    movie = db.get_by_id(movie_id)
    form = MovieFormRate(obj=movie)
    if form.validate_on_submit():
        movie.rating = form.rating.data
        movie.review = form.review.data
        db.update(movie)
        db.update_rankings()

        return redirect(url_for("home"))

    return render_template("edit.html", movie=movie, form=form)


@app.route('/delete/<int:movie_id>', methods=['POST'])
def delete(movie_id):
    if request.method == "POST":
        db.delete(movie_id)
        db.update_rankings()

    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
