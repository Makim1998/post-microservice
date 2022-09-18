from main import Session, engine
from model import User

local_session = Session(bind=engine)
user = User(username="nenafata", email='ahahahah')
local_session.add(user)
local_session.commit()
