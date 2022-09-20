from pydantic import BaseModel
from typing import Union


class UserDTO(BaseModel):
    id: int
    profile_id: int
    name: str
    surname: str
    email: Union[str, None] = None
    password: Union[str, None] = None
    role: str


class PostDTO(BaseModel):
    id: int
    text: str
    picture: str
    date: str
    user_id: int
    name: str
    surname: str


class PostCreateDTO(BaseModel):
    text: str
    picture: str
    user_id: int


class CommentCreateDTO(BaseModel):
    id: int
    user_id: int
    post_id: int
    text: str


class CommentDTO(BaseModel):
    id: int
    user_id: int
    post_id: int
    text: str
    name: str
    surname: str


class ReactionDTO(BaseModel):
    id: int
    like: bool
    user_id: int
    post_id: int


class ProfileUser(BaseModel):
    id: int
    email: str
    username: str
    password: str
    ime: str
    prezime: str
    telefon: str
    datumRodjenja: str
    pol: str
