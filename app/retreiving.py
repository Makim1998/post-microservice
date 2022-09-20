from main import Session, engine
from model import User, Post

local_session = Session(bind=engine)

local_session.query(User).all()

def getPosts():
    return local_session.query(Post).all()



#users = local_session.query(User).orderBy(User.username).all()

#users = local_session.query(User).filter(User.username == "").first()

# za update izmenis ga i komitujes sesiju
# testiranje 
