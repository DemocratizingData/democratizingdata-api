import pytest
from unittest.mock import MagicMock
from fastapi.testclient import TestClient
from democratizing.dependencies import get_db
from democratizing.main import app


@pytest.fixture
def mock_db():
    mock_result = MagicMock()
    yield mock_result


@pytest.fixture
def test_client(mock_db):
    """
    test_client fixture that provides a dependency override that bypasses
    JWT checking and returns a mocked profile
    """

    def mock_get_db():
        return mock_db

    app.dependency_overrides[get_db] = mock_get_db
    return TestClient(app)
