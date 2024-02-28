from fastapi.testclient import TestClient

from fastapi_neon.main import app

client = TestClient(app=app)

# https://fastapi.tiangolo.com/tutorial/testing/

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

def test_write_main():
    response = client.post("/todos/",
        json={"content": "buy apples"}
    )
    assert response.status_code == 200

def test_read_list_main():
    response = client.get("/todos/")
    assert response.status_code == 200
    