import pytest
from app.conf_test_db import app
from fastapi.testclient import TestClient
import json 

def test_get_root():
    with TestClient(app=app, base_url="http://test") as client:
        response = client.get("/")
    assert response.status_code == 200

def test_get_posts():
    print("--------------------------------------------\n")
    with TestClient(app=app, base_url="http://test") as client:
        response = client.get("/post")
        body = json.loads(response.text)
    print(response)
    print("-----------\n")
    print(body[1])
    print("------------")
    assert response.status_code == 200
    assert body[1]['id'] == 2
    assert body[1]['text'] == 'Zalazak test'
    assert body[1]['name'] == 'Test'

def test_public_posts():
    with TestClient(app=app, base_url="http://test") as client:
        response = client.get("/post/public")
        body = json.loads(response.text)
    print("-----------\n")
    print(body[0])
    print("------------")
    assert response.status_code == 200
    assert body[0]['text'] == 'Zalazak test'
    assert body[0]['name'] == 'Test'

def test_comments_for_post_found():
    with TestClient(app=app, base_url="http://test") as client:
        response = client.get("/comments/1")
        body = json.loads(response.text)
    print("-----------\n")
    print(body[0])
    print("------------")
    assert response.status_code == 200
    assert body[0]['text'] == 'nije lep dan test'
    assert body[0]['name'] == 'Nikola'

def test_comments_for_post_not_found():
    with TestClient(app=app, base_url="http://test") as client:
        response = client.get("/comments/111")
        body = json.loads(response.text)
    print("-----------\n")
    print(body)
    print("------------")
    assert response.status_code == 200
    assert len(body) == 0

def test_user():
    with TestClient(app=app, base_url="http://test") as client:
        response = client.get("/user/4")
        body = json.loads(response.text)
    print("-----------\n")
    print(body)
    print("------------")
    assert response.status_code == 200
    assert body['surname'] == 'Testic'
    assert body['name'] == 'Test'

"""def test_user_not_found():
    with TestClient(app=app, base_url="http://test") as client:
        response = client.get("/user/666")
        body = json.loads(response.text)
    print("-----------\n")
    print(body)
    print("------------")
    assert response.status_code == 200
    assert len(body) == 0"""

if __name__ == '__main__':
    test_get_posts()