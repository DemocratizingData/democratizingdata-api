from democratizing.publications.crud import get_publications
from democratizing.schemas import Publication
from democratizing.dependencies import PaginationParams


def test_get_publications(integration_db_session):
    result = Publication.from_orm(
        get_publications(PaginationParams(limit=1, offet=0), integration_db_session)[0]
    )
    assert result.id is not None
