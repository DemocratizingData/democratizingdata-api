from democratizing.affiliations.crud import get_affiliations
from democratizing.schemas import Affiliation
from democratizing.dependencies import PaginationParams


def test_get_affiliations(integration_db_session):
    result = Affiliation.from_orm(
        get_affiliations(PaginationParams(limit=1, offet=0), integration_db_session)[0]
    )
    assert result.id is not None
