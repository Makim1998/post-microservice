from fastapi import APIRouter, Depends
from app.dto import CommentDTO, CommentCreateDTO
from typing import List
from app.services.comment_service import get_comments, add_comment

from sqlalchemy.orm import Session
from app.create_db import get_db

router = APIRouter()


@router.get("/comments/{post_id}", response_model=List[CommentDTO], tags=["comment"])
async def get_comments_for_post(post_id, database: Session = Depends(get_db)):
    return get_comments(post_id, database)


@router.post("/comments", response_model=CommentCreateDTO, tags=["comment"])
async def add(comment: CommentCreateDTO, database: Session = Depends(get_db)):
    return add_comment(comment, database)