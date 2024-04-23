from flask_sqlalchemy import SQLAlchemy

from movie import Movie

DB_URI = "sqlite:///movies_collection.db"


class MoviesDB:

    def __init__(self, app):
        self.app = app
        self.app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
        self.db = SQLAlchemy(model_class=Movie)
        self.db.init_app(app)
        self.create()

    def create(self):
        with self.app.app_context():
            self.db.create_all()

    def add(self, movie: Movie):
        with self.app.app_context():
            self.db.session.add(movie)
            self.db.session.commit()

    def get_all(self):
        with self.app.app_context():
            movies = self.db.session.execute(
                self.db.select(Movie).order_by(Movie.rating)).scalars().all()

            return movies

    def get_by_title(self, title):
        with self.app.app_context():
            movie = self.db.session.execute(
                self.db.select(Movie).where(Movie.title == title)).scalar()

            return movie

    def get_by_id(self, movie_id):
        with self.app.app_context():
            movie = self.db.session.execute(
                self.db.select(Movie).where(Movie.id == movie_id)).scalar()

            return movie

    def update(self, movie: Movie):
        with self.app.app_context():
            movie_to_update = self.db.session.execute(
                self.db.select(Movie).where(Movie.id == movie.id)).scalar()
            # or movie_to_update = self.db.get_or_404(Movie, movie.id)
            movie_to_update.title = movie.title
            movie_to_update.year = movie.year
            movie_to_update.description = movie.description
            movie_to_update.rating = movie.rating
            movie_to_update.ranking = movie.ranking
            movie_to_update.review = movie.review
            movie_to_update.img_url = movie.img_url
            self.db.session.commit()

    def update_rankings(self):
        with self.app.app_context():
            all_movies = self.db.session.execute(
                self.db.select(Movie).order_by(
                    Movie.rating)).scalars().all()
            movies_len = len(all_movies)
            for i in range(movies_len):
                all_movies[i].ranking = movies_len - i
            self.db.session.commit()

    def delete(self, movie_id):
        with self.app.app_context():
            movie_to_delete = self.db.session.execute(
                self.db.select(Movie).where(Movie.id == movie_id)).scalar()
            # or movie_to_delete = self.db.get_or_404(Movie, movie_id)
            self.db.session.delete(movie_to_delete)
            self.db.session.commit()
