import pytest
from main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client
def test_index_page(client):
    response = client.get('/')
    assert response.status_code == 200
def test_login_page(client):            
    response = client.get('/login')
    assert response.status_code == 405    # Method Not Allowed for GET request
def test_login_post(client):
    response = client.post('/login', data={'username': 'user', 'password': 'user'})
    assert response.status_code == 200
    assert b'success' in response.data
def test_logout(client):
    with client.session_transaction() as session:
        session['type'] = 'user'
    response = client.get('/logout')
    assert response.status_code == 302  # Redirect status code
         

     




   