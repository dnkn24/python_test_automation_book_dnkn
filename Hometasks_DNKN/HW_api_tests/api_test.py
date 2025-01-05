from sys import excepthook

import pytest
import requests


from jsonschema import validate
from jsonschema.exceptions import ValidationError
from unittest.mock import Mock, patch

# Define the schema for validating the post response
schema = {
    "type": "object",
    "properties": {
        "userId": {"type": "integer"},
        "id": {"type": "integer"},
        "title": {"type": "string"},
        "body": {"type": "string"}
    },
    "required": ["userId", "id", "title", "body"]
}

# Pytest fixture to provide base URL
@pytest.fixture(scope="module")
def base_url():
    return "https://jsonplaceholder.typicode.com"

# Pytest fixture to provide headers with no authorization
@pytest.fixture(scope="module")
def headers_with_no_auth():
    return {"Content-Type": "application/json"}

# Pytest fixture to provide headers with authorization
@pytest.fixture(scope="module")
def headers():
    return {
        "Content-Type": "application/json",
        "Authorization": "8dde0e87ea2e654e1ac20906275ac03c_207171_1736118933654_1"
    }


# Pytest fixture to provide dummy data for creating a new post
@pytest.fixture(scope="module")
def new_post_payload():
    return {
        "userId": 1,
        "title": "Test Title",
        "body": "Test Body"
    }

@pytest.fixture(scope="module")
def updated_payload(new_post_payload):
    updated_payload = new_post_payload.copy()
    updated_payload["title"] = "Updated Title"
    return updated_payload


# Test GET request
@pytest.mark.parametrize("post_id", [1, 2, 3])
def test_get_post(base_url, headers_with_no_auth, post_id):
    # Test to get a post and validate its structure and data
    response = requests.get(f"{base_url}/posts/{post_id}", headers=headers_with_no_auth)
    assert response.status_code == 200
    assert response.json()["id"] == post_id
    try:
        validate(instance=response.json(), schema=schema)
    except ValidationError as e:
        pytest.fail(f"Response validation failed: {e}")


# Test POST request
def test_create_post(base_url, headers_with_no_auth, new_post_payload):
    # Test creating a new post and verifying the response code and payload
    response = requests.get(f"{base_url}/posts/", headers=headers_with_no_auth)
    assert response.status_code == 200
    posts = response.json()
    assert isinstance(posts, list)
    num_posts = len(posts)
    response = requests.post(f"{base_url}/posts", headers=headers_with_no_auth, json=new_post_payload)
    assert response.status_code == 201
    try:
        validate(instance=response.json(), schema=schema)
    except ValidationError as e:
        pytest.fail(f"Response validation failed: {e}")
    response_data = response.json()
    assert response_data["title"] == new_post_payload["title"]
    assert response_data["body"] == new_post_payload["body"]
    assert response_data["userId"] == new_post_payload["userId"]
    assert response_data["id"] == num_posts + 1



# Test for PUT request
@pytest.mark.parametrize("post_id", [1])
def test_update_post(base_url, headers_with_no_auth, post_id, updated_payload):
    # Test updating a post and checking for proper updates
    response = requests.put(f"{base_url}/posts/{post_id}", headers=headers_with_no_auth, json=updated_payload)
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["title"] == "Updated Title"

# Test for DELETE request
@pytest.mark.parametrize("post_id", [155]) # 155 is a non-existing post ID in order to add assertion step for 404
def test_delete_post(base_url, headers_with_no_auth, post_id):
    # Test deleting a post and confirming its removal
    response = requests.delete(f"{base_url}/posts/{post_id}", headers=headers_with_no_auth)
    assert response.status_code == 200
    response = requests.get(f"{base_url}/posts/{post_id}", headers=headers_with_no_auth)
    assert response.status_code == 404
    assert response.json() == {}

# Mock tests
@patch('requests.get')
def test_mock_get_post(mock_get, base_url, headers_with_no_auth):
    # Mock test for successful GET request
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "userId": 1, "id": 1, "title": "Mock Title", "body": "Mock Body"
    }
    response = requests.get(f"{base_url}/posts/1", headers=headers_with_no_auth)
    assert response.status_code == 200
    assert response.json()["title"] == "Mock Title"
    assert response.json()["body"] == "Mock Body"
    assert response.json()["userId"] == 1
    assert response.json()["id"] == 1

@patch('requests.put')
def test_mock_put_post(mock_put, base_url, headers_with_no_auth, updated_payload):
    # Mock test for successful GET request
    mock_put.return_value.status_code = 200
    mock_put.return_value.json.return_value = {
        "userId": 1, "id": 1, "title": "Mock Updated Title", "body": "Mock Updated Body"
    }
    response = requests.put(f"{base_url}/posts/1", headers=headers_with_no_auth, json= updated_payload)
    assert response.status_code == 200
    assert response.json()["title"] == "Mock Updated Title"
    assert response.json()["body"] == "Mock Updated Body"
    assert response.json()["userId"] == 1
    assert response.json()["id"] == 1

@patch('requests.delete')
def test_mock_delete_post_error(mock_delete, base_url, headers_with_no_auth):
    # Mock test for unsuccessful DELETE request
    mock_delete.return_value.status_code = 500
    response = requests.delete(f"{base_url}/posts/155", headers=headers_with_no_auth)
    assert response.status_code == 500

