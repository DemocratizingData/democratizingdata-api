import pytest
from unittest.mock import MagicMock
from fastapi.testclient import TestClient
from democratizing.dependencies import get_db
from democratizing.main import app
from democratizing import models, schemas
from democratizing.database import SessionLocal
from pydantic import BaseModel
import os
import json


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
    yield TestClient(app)


@pytest.fixture
def mock_publication_model():
    entry = {
        "id": 61,
        "run_id": 1,
        "journal_id": 16,
        "external_id": "2-s2.0-85087111976",
        "title": "Space is more important than season when shaping soil microbial communities at a large spatial scale",
        "doi": "10.1128/mSystems.00783-19",
        "year": 2020,
        "month": 6,
        "pub_type": "Article",
        "citation_count": 21,
        "fw_citation_impact": 3.8,
    }
    yield models.Publication(**entry)


@pytest.fixture
def integration_db_session():
    yield SessionLocal()


def load_schema_from_fixture(schema: BaseModel, fixture: str):
    with open(os.path.join(os.path.dirname(__file__), f"fixtures/{fixture}"), "r") as f:
        return schema(**json.load(f))


@pytest.fixture
def topic_schema():
    yield load_schema_from_fixture(schemas.Topic, "topic.json")


@pytest.fixture
def publication_schema():
    yield load_schema_from_fixture(schemas.Publication, "publication.json")
