from fastapi import APIRouter
from app.services.user_service import getUserById
from app.dto import UserDTO

router = APIRouter()


@router.get("/user/{id}", response_model=UserDTO, tags=["user"])
async def get_user(id):
    return getUserById(id)