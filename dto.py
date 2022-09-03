from pydantic import BaseModel


class PostDTO(BaseModel):
    id: int
    text: str
    picture: str
    date: str
    name: str
    surname: str


class CommentDTO(BaseModel):
    id: int
    text: str
    name: str
    surname: str

