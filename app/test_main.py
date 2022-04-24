from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)

def test_hello_world():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

def test_calculate():
    response = client.post(
        "/calculate/",
        json={'dims': [2,2], 'rectangle': [[1,1], [1,0], [0,1], [0,0]]}
    )
    assert response.json() == [[[0., 1.], [1., 1.]], [[0., 0.], [1., 0.]]]