from democratizing.publishers.crud import get_publishers
from democratizing.schemas import Publisher
from democratizing.dependencies import PaginationParams


def test_get_publishers(integration_db_session):
    result = Publisher.from_orm(
        get_publishers(PaginationParams(limit=1, offet=0), integration_db_session)[0]
    )
    assert result.id is not None
