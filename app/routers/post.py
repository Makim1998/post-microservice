from fastapi import APIRouter
from app.dto import PostDTO, PostCreateDTO
from typing import List
from app.services.post_service import get_all_posts, get_public_posts, get_following_posts, get_user_posts, add_post
from .auth import validate_auth
from app.dto import UserDTO
from fastapi import Depends
import httpx
import json

router = APIRouter()

following_profiles_url = "http://localhost:8001/profile/following/"


@router.post("/post", response_model=PostCreateDTO, tags=["post"])
async def new_post(post: PostCreateDTO):
    return add_post(post)


@router.get("/post", response_model=List[PostDTO], tags=["post"])
async def all_posts():
    return get_all_posts()


@router.get("/post/public", response_model=List[PostDTO], tags=["post"])
async def public_posts():
    return get_public_posts()


@router.get("/post/{user_id}", response_model=List[PostDTO], tags=["post"])
async def user_posts(user_id):
    return get_user_posts(user_id)


@router.get("/post/following/{profile_id}", response_model=List[PostDTO], tags=["post"])
async def followers_posts(profile_id):
    # dobavi prvo pratioce iz mikroservisa sa profilima
    async with httpx.AsyncClient() as client:
        response = await client.get(following_profiles_url + profile_id)
        print(json.loads(response.text))
        return get_following_posts(json.loads(response.text))
