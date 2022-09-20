from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer(), primary_key=True)
    name = Column(String(25), nullable=False)
    surname = Column(String(25), nullable=False)
    picture = Column(String(25))
    private = Column(Boolean)
    role = Column(String(25), nullable=False)
    posts = relationship("Post", back_populates="author")
    reactions = relationship("Reaction", back_populates="author")  # bitno da proverimo da li je vec reagovao na neki post



class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer(), primary_key=True)
    date = Column(DateTime(), default=datetime.utcnow)
    text = Column(String())
    picture = Column(String())
    author_id = Column(Integer, ForeignKey("users.id"))
    author = relationship("User", back_populates="posts")
    reactions = relationship("Reaction", back_populates="post")
    comments = relationship("Comment", back_populates="post")
    likes = Column(Integer())
    dislikes = Column(Integer())


class Reaction(Base):
    __tablename__ = "reactions"
    id = Column(Integer(), primary_key=True)
    like = Column(Boolean())
    post_id = Column(Integer, ForeignKey("posts.id"))
    post = relationship("Post", back_populates="reactions")
    author_id = Column(Integer, ForeignKey("users.id"))
    author = relationship("User", back_populates="reactions")


class Comment(Base):
    __tablename__ = "comments"
    id = Column(Integer(), primary_key=True)
    text = Column(String(80))
    post_id = Column(Integer, ForeignKey("posts.id"))
    post = relationship("Post", back_populates="comments")
    author_id = Column(Integer, ForeignKey("users.id"))


