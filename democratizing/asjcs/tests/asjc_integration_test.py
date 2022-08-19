from democratizing.asjcs.crud import get_asjcs
from democratizing.schemas import Asjc
from democratizing.dependencies import PaginationParams


def test_get_asjcs(integration_db_session):
    result = Asjc.from_orm(
        get_asjcs(PaginationParams(limit=1, offet=0), integration_db_session)[0]
    )
    assert result.code is not None
