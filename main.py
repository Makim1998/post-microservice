from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from dto import PostDTO, CommentDTO
from typing import List
import os
import uvicorn
from model import Post, Comment, User
from fastapi.responses import FileResponse

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
connection_string = "sqlite:///" + os.path.join(BASE_DIR, "site.db")

engine = create_engine(connection_string, echo=True)

Session = sessionmaker()

local_session = Session(bind=engine)


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_methods="*",
    allow_headers="*",
)


@app.get("/posts", response_model=List[PostDTO])
async def get_posts():
    print("merhaba")
    postsDTO = []
    for post in local_session.query(Post).all():
        postsDTO.append(PostDTO(id=post.id, picture=post.picture, text=post.text, date=post.date.strftime("%d/%m/%Y %H:%M"),
                                name=post.author.name, surname=post.author.surname))
        print(post.id)
    return postsDTO


@app.get("/images/{path}")
async def get_image(path):
    return FileResponse('imgs/' + path)


@app.get("/comments/{postId}")
async def get_comments_for_post(postId):
    commentsDTO = []
    for comment in local_session.query(Comment).filter(Comment.post_id == postId):
        author = local_session.query(User).filter(User.id == comment.author_id).first()
        commentsDTO.append(CommentDTO(id=comment.id, text=comment.text, name=author.name, surname=author.surname))
    return commentsDTO


@app.get("/")
async def root():
    return {"message": "Hello World"}

if __name__ == '__main__':
    uvicorn.run(app)
