from app.create_db import Session, engine
from app.model import Comment, User
from app.dto import CommentDTO, CommentCreateDTO

local_session = Session(bind=engine)


def get_comments(post_id):
    comments_dto = []
    for comment in local_session.query(Comment).filter(Comment.post_id == post_id):
        author = local_session.query(User).filter(User.id == comment.author_id).first()
        comments_dto.append(CommentDTO(id=comment.id, user_id=comment.author_id, post_id=comment.post_id,
                                       text=comment.text, name=author.name, surname=author.surname))
    return comments_dto


def add_comment(comment: CommentCreateDTO):
    comment_db = Comment(author_id=comment.user_id, post_id=comment.post_id,
                         text=comment.text)
    local_session.add(comment_db)
    local_session.commit()
    return comment


def delete_comment(comment_id: int):
    local_session.query(Comment).filter(Comment.id == comment_id).delete()
    local_session.commit()