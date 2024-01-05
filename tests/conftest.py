import pytest
from app import create_app


@pytest.fixture
def app():
    return create_app()

@pytest.fixture
def client(app):
    with app.test_client() as client:
        yield client
