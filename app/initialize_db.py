from sqlalchemy.sql import text
from create_db import engine

with engine.connect() as con:

    users = ({"id": 1, "name": "Admin", "surname": "Adminic",
              "picture": "sunce.jpg", "private": 0, "role": "admin"},
             {"id": 2, "name": "Ivan", "surname": "Ivanovic",
              "picture": "sunce.jpg", "private": 0, "role": "user"},
             {"id": 3, "name": "Nikola", "surname": "Nikolic",
              "picture": "sunce.jpg", "private": 1, "role": "user"},
             {"id": 4, "name": "Luka", "surname": "Lukic",
              "picture": "sunce.jpg", "private": 0, "role": "user"}
    )

    statement = text("""INSERT INTO users(id, name, surname, picture, private, role)
     VALUES(:id, :name, :surname, :picture, :private, :role)""")

    posts = ({"id": 1, "date": "'2022-08-01 09:01'", "text": "Sto je lep dan", "picture": "plazica.jpg", "author_id": "3"},
             {"id": 2, "date": "'2022-08-01 02:33'", "text": "Zalazak", "picture": "sunce.jpg", "author_id": "4"}
             )

    statement_posts = text("""INSERT INTO posts(id, date, text, picture, author_id)
     VALUES(:id, :date, :text, :picture, :author_id)""")

    comments = ({"id": 1, "text": "nije lep dan", "author_id": "3", "post_id": "1"},
                {"id": 2, "text": "lepa slika", "author_id": "4", "post_id": "1"}
                )

    statement_comments = text("""INSERT INTO comments(id, text, post_id, author_id)
         VALUES(:id, :text, :post_id, :author_id)""")

    for line in users:
        con.execute(statement, **line)

    for line in posts:
        con.execute(statement_posts, **line)

    for line in comments:
        con.execute(statement_comments, **line)






