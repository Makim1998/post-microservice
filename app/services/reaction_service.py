from app.create_db import Session, engine
from app.model import Reaction, User
from app.dto import ReactionDTO
local_session = Session(bind=engine)


def get_reactions(post_id: int):
    reactions_dto = []
    for reaction in local_session.query(Reaction).filter(Reaction.post_id == post_id):
        author = local_session.query(User).filter(User.id == reaction.author_id).first()
        reactions_dto.append(ReactionDTO(id=reaction.id, user_id=reaction.author_id, post_id=reaction.post_id,
                                         like=reaction.like, name=author.name, surname=author.surname))
    return reactions_dto


def add_reaction(reaction: ReactionDTO):
    reaction_db = Reaction(author_id=reaction.user_id, post_id=reaction.post_id,
                           like=reaction.like)
    local_session.add(reaction_db)
    local_session.commit()
    return reaction
