import requests

BASE_url = "https://jsonplaceholder.typicode.com/users"

def test_userstatus():
    response = requests.get(f"{BASE_url}/1")
    assert response.status_code == 200

def test_username():
    response = requests.get(f"{BASE_url}/1")
    data = response.json()
    assert data["name"] == "Leanne Graham"

def test_useremailaddress():
    response = requests.get(f"{BASE_url}/1")
    data = response.json()
    assert data["address"]["street"] == "Kulas Light"
    assert data["email"] == "Sincere@april.biz"

def test_usersstatus():
    response = requests.get(BASE_url)
    assert response.status_code == 200
    assert len(response.json()) == 10

def test_invaliduser():
    response = requests.get(f"{BASE_url}/999")
    assert response.status_code == 404