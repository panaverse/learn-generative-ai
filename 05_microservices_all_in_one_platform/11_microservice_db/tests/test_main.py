from fastapi.testclient import TestClient

# https://sqlmodel.tiangolo.com/tutorial/fastapi/tests/#override-a-dependency
from fastapi_neon.main import app, get_session

# https://fastapi.tiangolo.com/tutorial/testing/
# https://realpython.com/python-assert-statement/
# https://understandingdata.com/posts/list-of-python-assert-statements-for-unit-tests/

def test_read_main():
    client = TestClient(app=app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

def test_write_main():
    client = TestClient(app=app)

    todo_content = "buy bread"

    response = client.post("/todos/",
        json={"content": todo_content}
    )

    data = response.json()

    assert response.status_code == 200
    assert data["content"] == todo_content

def test_read_list_main():
    client = TestClient(app=app)

    response = client.get("/todos/")
    assert response.status_code == 200
    