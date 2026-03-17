import pytest
import requests


base_url="https://jsonplaceholder.typicode.com"



def test_get_users():

  response = requests.get(f"{base_url}/users")
  assert response.status_code == 200
  assert isinstance(response.json(), list)



def test_get_user_by_id():

  response = requests.get(f"{base_url}/users/1")
  assert response.status_code == 200
  data = response.json()
  assert isinstance(data, dict)
  assert data["id"] == 1


# Test Posts Endpoint

def test_get_posts():

  response = requests.get(f"{base_url}/posts")
  assert response.status_code == 200
  assert isinstance(response.json(), list)



def test_get_post_by_id():

  response = requests.get(f"{base_url}/posts/1")
  assert response.status_code == 200
  data = response.json()
  assert isinstance(data, dict)
  assert data["id"] == 1



# Test Comments Endpoint

def test_get_comments():

  response = requests.get(f"{base_url}/comments")
  assert response.status_code == 200
  assert isinstance(response.json(), list)

def test_get_comment_by_id():

  response = requests.get(f"{base_url}/comments/1")
  assert response.status_code == 200
  data = response.json()
  assert isinstance(data, dict)
  assert data["id"] == 1

# Test Albums Endpoint
@pytest.mark.api
def test_get_albums():

  response = requests.get(f"{base_url}/albums")
  assert response.status_code == 200
  assert isinstance(response.json(), list)

@pytest.mark.api
def test_get_album_by_id():
  response = requests.get(f"{base_url}/albums/1")
  assert response.status_code == 200
  data = response.json()
  assert isinstance(data, dict)
  assert data["id"] == 1

# Test Photos Endpoint
@pytest.mark.api
def test_get_photos():
  response = requests.get(f"{base_url}/photos")
  assert response.status_code == 200
  assert isinstance(response.json(), list)

@pytest.mark.api
def test_get_photo_by_id():
  response = requests.get(f"{base_url}/photos/1")
  assert response.status_code == 200
  data = response.json()
  assert isinstance(data, dict)
  assert data["id"] == 1

# Test Todos Endpoint
@pytest.mark.api
def test_get_todos():
  response = requests.get(f"{base_url}/todos")
  assert response.status_code == 200
  assert isinstance(response.json(), list)

@pytest.mark.api
def test_get_todo_by_id():
  response = requests.get(f"{base_url}/todos/1")
  assert response.status_code == 200
  data = response.json()
  assert isinstance(data, dict)
  assert data["id"] == 1



