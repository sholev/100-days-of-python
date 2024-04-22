from flask_sqlalchemy import SQLAlchemy

from book import Book

DB_URI = "sqlite:///books_collection.db"


class BooksDB:

    def __init__(self, app):
        self.app = app
        self.app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
        self.db = SQLAlchemy(model_class=Book)
        self.db.init_app(app)
        self.create()

    def create(self):
        with self.app.app_context():
            self.db.create_all()

    def add(self, title, author, rating):
        with self.app.app_context():
            new_book = Book(title=title, author=author, rating=rating)
            self.db.session.add(new_book)
            self.db.session.commit()

    def get_all(self):
        with self.app.app_context():
            result = self.db.session.execute(
                self.db.select(Book).order_by(Book.title))
            all_books = result.scalars().all()

            return all_books

    def get_by_title(self, title):
        with self.app.app_context():
            book = self.db.session.execute(
                self.db.select(Book).where(Book.title == title)).scalar()

            return book

    def get_by_id(self, book_id):
        with self.app.app_context():
            book = self.db.session.execute(
                self.db.select(Book).where(Book.id == book_id)).scalar()

            return book

    def update_tittle(self, title_old, title_new):
        with self.app.app_context():
            book_to_update = self.db.session.execute(
                self.db.select(Book).where(Book.title == title_old)).scalar()
            book_to_update.title = title_new
            self.db.session.commit()

    def update(self, book_id, title, author, rating):
        with self.app.app_context():
            book_to_update = self.db.session.execute(
                self.db.select(Book).where(Book.id == book_id)).scalar()
            # or book_to_update = db.get_or_404(Book, book_id)
            book_to_update.title = title
            book_to_update.author = author
            book_to_update.rating = rating
            self.db.session.commit()

    def delete(self, book_id):
        with self.app.app_context():
            book_to_delete = self.db.session.execute(
                self.db.select(Book).where(Book.id == book_id)).scalar()
            # or book_to_delete = db.get_or_404(Book, book_id)
            self.db.session.delete(book_to_delete)
            self.db.session.commit()
