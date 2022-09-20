from app.create_db import engine
from app.model import Reaction, User
from app.dto import ReactionDTO
from fastapi import Depends
from sqlalchemy.orm import Session
from app.create_db import get_db

#local_session = Session(bind=engine)
#local_session: Session = Depends(get_db)

def get_reactions(post_id: int, database):
    reactions_dto = []
    for reaction in database.query(Reaction).filter(Reaction.post_id == post_id):
        author = database.query(User).filter(User.id == reaction.author_id).first()
        reactions_dto.append(ReactionDTO(id=reaction.id, user_id=reaction.author_id, post_id=reaction.post_id,
                                         like=reaction.like, name=author.name, surname=author.surname))
    return reactions_dto


def add_reaction(reaction: ReactionDTO, database):
    reaction_db = Reaction(author_id=reaction.user_id, post_id=reaction.post_id,
                           like=reaction.like)
    database.add(reaction_db)
    database.commit()
    return reaction
