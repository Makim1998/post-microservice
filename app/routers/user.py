from fastapi import APIRouter, Depends
from app.services.user_service import getUserById
from app.dto import UserDTO

from sqlalchemy.orm import Session
from app.create_db import get_db

router = APIRouter()


@router.get("/user/{id}", response_model=UserDTO, tags=["user"])
async def get_user(id, database: Session = Depends(get_db)):
    return getUserById(id, database)