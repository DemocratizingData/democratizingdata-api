from democratizing.authors.crud import get_authors
from democratizing.schemas import Author
from democratizing.dependencies import PaginationParams


def test_get_authors(integration_db_session):
    result = Author.from_orm(
        get_authors(PaginationParams(limit=1, offet=0), integration_db_session)[0]
    )
    assert result.id is not None
