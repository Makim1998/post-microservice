from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
# from app.create_db import Session, engine
from fastapi import Depends
from sqlalchemy.orm import Session
from app.create_db import get_db

import uvicorn
from app.routers import auth, comment, post, reaction, image, user
from model import User
from dto import ProfileUser

# local_session = Session(bind=engine)


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_methods="*",
    allow_headers="*",
)

app.include_router(post.router)
app.include_router(comment.router)
app.include_router(reaction.router)
app.include_router(image.router)
app.include_router(user.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/register")
async def save_user(request: ProfileUser, database: Session = Depends(get_db)):
    user = User()
    user.id = request.id
    user.name = request.ime
    user.surname = request.prezime
    user.private = False
    user.picture = ''
    user.role = "user"

    database.add(user)
    database.commit()




if __name__ == '__main__':
    uvicorn.run(app, port=8000, host="0.0.0.0")
