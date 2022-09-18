from app.create_db import Session, engine
from app.model import User
from app.dto import UserDTO

local_session = Session(bind=engine)


def getUserById(id):
    user = local_session.query(User).filter(User.id == id).first()
    userDTO = UserDTO(id=user.id, profile_id=user.id, name=user.name,
                      surname=user.surname, email="", password="", role=user.role)
    return userDTO
