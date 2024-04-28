from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text, ForeignKey
from flask_login import UserMixin


class Base(DeclarativeBase):
    pass


class User(UserMixin, Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    username: Mapped[str] = mapped_column(String(100))

    posts: Mapped[list["BlogPost"]] = relationship(back_populates="author")

    comments: Mapped[list["Comment"]] = relationship("Comment", back_populates="author")


class BlogPost(Base):
    __tablename__ = "blog_posts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

    author_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'))
    author: Mapped[User] = relationship("User", back_populates="posts")

    comments: Mapped[list["Comment"]] = relationship("Comment", back_populates="post")


class Comment(Base):
    __tablename__ = "comments"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    text: Mapped[str] = mapped_column(Text, nullable=False)

    author_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    author: Mapped[User] = relationship("User", back_populates="comments")

    post_id: Mapped[str] = mapped_column(Integer, ForeignKey("blog_posts.id"))
    post: Mapped[BlogPost] = relationship("BlogPost", back_populates="comments")

