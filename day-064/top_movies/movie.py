from sqlalchemy import Integer, String, Float, SmallInteger
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.ext.declarative import declarative_base


class Movie(declarative_base()):
    __tablename__ = "movies"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(500), unique=True,
                                       nullable=False)
    year: Mapped[int] = mapped_column(SmallInteger)
    description: Mapped[str] = mapped_column(String(), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
    ranking: Mapped[int] = mapped_column(Integer)
    review: Mapped[str] = mapped_column(String(), nullable=False)
    img_url: Mapped[str] = mapped_column(String(), nullable=False)

    def __repr__(self):
        return f'<Movie_{self.title}_{self.year}>'
