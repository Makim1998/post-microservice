from app.create_db import engine
from app.model import User
from app.dto import UserDTO
from fastapi import Depends
from sqlalchemy.orm import Session
from app.create_db import get_db

#local_session = Session(bind=engine)
#local_session: Session = Depends(get_db)

def getUserById(id, database):
    user = database.query(User).filter(User.id == id).first()
    userDTO = UserDTO(id=user.id, profile_id=user.id, name=user.name,
                      surname=user.surname, email="", password="", role=user.role)
    return userDTO
