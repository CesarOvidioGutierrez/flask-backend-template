import json
from http import HTTPStatus

from tests import fake_user
from app.config.constants import INVALID_CREDENTIALS

expected_fields = ['email', 'firstName', 'lastName', 'token']

def test_authentication_with_fixture(client, valid_credentials):
    response = client.post('/api/auth', data=json.dumps(valid_credentials), content_type='application/json')
    
    assert response.status_code == HTTPStatus.OK
    

    for field in expected_fields:
        assert field in response.json

def test_invalid_validation_credentials(client):
    email, password = fake_user()
    response = client.post('/api/auth', data=json.dumps({'email': email, 'password': password}), content_type='application/json')
    
    assert response.status_code == HTTPStatus.UNAUTHORIZED  

    assert 'message' in response.json
    assert response.json.get('message') == INVALID_CREDENTIALS

