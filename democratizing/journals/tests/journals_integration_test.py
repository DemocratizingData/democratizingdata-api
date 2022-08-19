from democratizing.journals.crud import get_journals
from democratizing.schemas import Journal
from democratizing.dependencies import PaginationParams


def test_get_journals(integration_db_session):
    result = Journal.from_orm(
        get_journals(PaginationParams(limit=1, offet=0), integration_db_session)[0]
    )
    assert result.title is not None
