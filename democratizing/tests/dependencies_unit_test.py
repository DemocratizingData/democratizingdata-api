import pytest
from fastapi import FastAPI, Depends, APIRouter
from fastapi.testclient import TestClient
from democratizing.dependencies import get_pagination_params, PaginationParams
from unittest.mock import MagicMock


pagination_spy = MagicMock()


@pytest.fixture
def dependency_test_router():
    pagination_spy.reset_mock()
    dependency_test_router = APIRouter(
        prefix="/test",
        tags=["test"],
        responses={404: {"description": "Not found"}},
    )

    @dependency_test_router.get("")
    def test(pagination: PaginationParams = Depends(get_pagination_params)):
        pagination_spy(pagination)
        return {}

    yield dependency_test_router


@pytest.fixture
def dependency_test_client(dependency_test_router):
    app = FastAPI()
    app.include_router(dependency_test_router)
    client = TestClient(app)
    yield client


def test_pagination_dependency(dependency_test_client):
    dependency_test_client.get("/test?limit=20&offset=10")
    pagination_spy.assert_called_with(PaginationParams(limit=20, offset=10))
