from fastapi import APIRouter, Depends
from app.services.reaction_service import get_reactions, add_reaction
from typing import List
from app.dto import ReactionDTO

from sqlalchemy.orm import Session
from app.create_db import get_db

router = APIRouter()


@router.get("/reaction/{postId}", response_model=List[ReactionDTO], tags=["reaction"])
async def get_reactions_for_post(postId, database: Session = Depends(get_db)):
    return get_reactions(postId, database)


@router.post("/reaction", response_model=ReactionDTO, tags=["reaction"])
async def reaction_new(reaction: ReactionDTO, database: Session = Depends(get_db)):
    return add_reaction(reaction, database)