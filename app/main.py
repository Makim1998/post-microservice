from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

import uvicorn
from app.routers import auth, comment, post, reaction, image, user


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


if __name__ == '__main__':
    uvicorn.run(app, port=8000, host="0.0.0.0")
