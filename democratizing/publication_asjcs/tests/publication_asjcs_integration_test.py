from democratizing.publication_authors.crud import get_publication_authors
from democratizing.schemas import PublicationAuthor
from democratizing.dependencies import PaginationParams


def test_get_publication_authors(integration_db_session):
    result = PublicationAuthor.from_orm(
        get_publication_authors(
            PaginationParams(limit=1, offet=0), integration_db_session
        )[0]
    )
    assert result.publication_id is not None
