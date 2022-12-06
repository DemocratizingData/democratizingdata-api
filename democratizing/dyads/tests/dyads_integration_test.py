from democratizing.dyads.crud import (
    get_dyads,
)
from democratizing.schemas import Dyad
from democratizing.dependencies import PaginationParams


def test_get_dyads(integration_db_session):
    result = Dyad.from_orm(
        get_dyads(
            PaginationParams(limit=1, offet=0), integration_db_session
        )[0]
    )
    assert result.publication_id is not None
