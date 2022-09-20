from app.create_db import engine
from app.model import Comment, User
from app.dto import CommentDTO, CommentCreateDTO
from fastapi import Depends
from sqlalchemy.orm import Session
from app.create_db import get_db

#local_session = Session(bind=engine)
#local_session: Session = Depends(get_db)

def get_comments(post_id, database):
    comments_dto = []
    for comment in database.query(Comment).filter(Comment.post_id == post_id):
        author = database.query(User).filter(User.id == comment.author_id).first()
        comments_dto.append(CommentDTO(id=comment.id, user_id=comment.author_id, post_id=comment.post_id,
                                       text=comment.text, name=author.name, surname=author.surname))
    return comments_dto


def add_comment(comment: CommentCreateDTO, database):
    comment_db = Comment(author_id=comment.user_id, post_id=comment.post_id,
                         text=comment.text)
    database.add(comment_db)
    database.commit()
    return comment


def delete_comment(comment_id: int, database):
    database.query(Comment).filter(Comment.id == comment_id).delete()
    database.commit()