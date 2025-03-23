import requests
import pytest

URL = "https://jsonplaceholder.typicode.com"

def test_create_post():
    url = f"{URL}/posts"
    data = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }
    response = requests.post(url, json=data)
    assert response.status_code == 201
    assert response.json()["title"] == "foo"

def test_update_post():
    post_id = 1
    url = f"{URL}/posts/{post_id}"
    data = {
        "title": "updated title",
        "body": "updated body"
    }
    response = requests.put(url, json=data)
    assert response.status_code == 200
    assert response.json()["title"] == "updated title"

def test_delete_post():
    post_id = 1
    url = f"{   URL}/posts/{post_id}"
    response = requests.delete(url)
    assert response.status_code == 200
