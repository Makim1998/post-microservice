from fastapi import APIRouter
from app.services.reaction_service import get_reactions, add_reaction
from typing import List
from app.dto import ReactionDTO


router = APIRouter()


@router.get("/reaction/{postId}", response_model=List[ReactionDTO], tags=["reaction"])
async def get_reactions_for_post(postId):
    return get_reactions(postId)


@router.post("/reaction", response_model=ReactionDTO, tags=["reaction"])
async def reaction_new(reaction: ReactionDTO):
    return add_reaction(reaction)