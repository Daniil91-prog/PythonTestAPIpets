import pytest

from utils.api_client import ApiClient

BASE_URL = "https://petstore.swagger.io/v2"
# pet_id = 2222
# pet_name = "bobik"
# pen_new_name = "bob"

@pytest.fixture
def api_client():
    return ApiClient(BASE_URL)

def test_create_pet(api_client):
    data = {
        "id": 2222,
        "name": "bobik",
        "photoUrls": ["http://example.com/photo.jpg"],
        "status": "available"
    }

    response = api_client.post("/pet", data=data)
    assert response.status_code == 200
    assert response.json()['name'] == 'bobik'

def test_get_pet(api_client):
    response = api_client.get("/pet/2222")
    assert response.status_code == 200
    assert response.json()['id'] == 2222
    assert response.json()['name'] == 'bob'

def test_update_pet(api_client):
    data = {
        "id": 2222,
        "name": "bob",
        "photoUrls": ["http://example.com/photo.jpg"],
        "status": "available"
    }

    response = api_client.put("/pet", data=data)
    assert response.status_code == 200
    assert response.json()['name'] == 'bob'

def test_delete_pet(api_client):
    response = api_client.delete("/pet/2222")
    assert response.status_code == 200

def test_get_pet_negative(api_client):
    response = api_client.get("/pet/2222455")
    assert response.status_code == 404

















