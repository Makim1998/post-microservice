from fastapi import APIRouter
from app.dto import CommentDTO, CommentCreateDTO
from typing import List
from app.services.comment_service import get_comments, add_comment

router = APIRouter()


@router.get("/comments/{post_id}", response_model=List[CommentDTO], tags=["comment"])
async def get_comments_for_post(post_id):
    return get_comments(post_id)


@router.post("/commenst", response_model=CommentCreateDTO, tags=["comment"])
async def add(comment: CommentCreateDTO):
    return add_comment(comment)
