from app import app

def test_hello_world():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert response.data == b'<h1>Hello Renny, soy yo, Grecia, desde mi API!<h1>'