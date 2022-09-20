import unittest
#from unittest.mock import MagicMock
#from app.services.comment_service import get_comments
#from fastapi.testclient import TestClient
#import json 
#from app.main import app

#get_comments = MagicMock(return_value=[])

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)  # add assertion here

"""def test_get_comments_for_post():
    get_comments = MagicMock(return_value=[])
    with TestClient(app=app, base_url="http://test") as client:
        get_comments = MagicMock(return_value=[])
        response = client.get("/comment/1")
        body = json.loads(response.text)
    print("-----------\n")
    print(body)
    print("------------")"""

if __name__ == '__main__':
    unittest.main()