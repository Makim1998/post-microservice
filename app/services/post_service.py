from app.create_db import engine
from app.model import Post
from app.dto import PostDTO, PostCreateDTO
from datetime import datetime
from fastapi import Depends
from sqlalchemy.orm import Session
from app.create_db import get_db

#local_session = Session(bind=engine)
#local_session: Session = Depends(get_db)

def get_all_posts(database):
    posts_db = database.query(Post).order_by(Post.date.desc()).all()
    return map_db_dto(posts_db)


def get_public_posts(database):
    posts_db = database.query(Post).order_by(Post.date.desc()).all()
    public_posts_db = []
    for post in posts_db:
        if not post.author.private:
            public_posts_db.append(post)
    return map_db_dto(public_posts_db)


def get_user_posts(user_id, database):
    posts_db = database.query(Post).filter(Post.author_id == user_id).order_by(Post.date.desc())
    return map_db_dto(posts_db)


def get_following_posts(followings, database):
    following_ids = []
    for following in followings:
        following_ids.append(following["user_id"])
    posts_db = database.query(Post).filter(Post.author_id.in_(following_ids)).order_by(Post.date.desc())
    print(posts_db)
    return map_db_dto(posts_db)


def add_post(post: PostCreateDTO, database):
    post_db = Post(author_id=post.user_id, picture=post.picture, text=post.text, date=datetime.now())
    database.add(post_db)
    database.commit()
    return post


def map_db_dto(posts_db):
    posts_dto = []
    for post in posts_db:
        posts_dto.append(
            PostDTO(id=post.id, user_id=post.author_id, picture=post.picture, text=post.text,
                    date=post.date.strftime("%d-%m-%Y %H:%M"),
                    name=post.author.name, surname=post.author.surname))
        print(post.id)
    return posts_dto