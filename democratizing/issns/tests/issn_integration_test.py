from democratizing.issns.crud import get_issns
from democratizing.schemas import ISSN
from democratizing.dependencies import PaginationParams


def test_get_asjcs(integration_db_session):
    result = ISSN.from_orm(
        get_issns(PaginationParams(limit=1, offet=0), integration_db_session)[0]
    )
    assert result.ISSN is not None
