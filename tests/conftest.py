import pytest
import os

from app import create_app
from app.config.constants import BASIC_AUTH_USERNAME, BASIC_AUTH_PASSWORD

@pytest.fixture
def valid_credentials():
    username = os.getenv(BASIC_AUTH_USERNAME)
    password = os.getenv(BASIC_AUTH_PASSWORD)
    return {'email': username, 'password': password}

@pytest.fixture
def app():
    return create_app()

@pytest.fixture
def client(app):
    with app.test_client() as client:
        yield client

