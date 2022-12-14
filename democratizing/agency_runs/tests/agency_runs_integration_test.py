from democratizing.agency_runs.crud import get_agency_runs
from democratizing.schemas import AgencyRun
from democratizing.dependencies import PaginationParams


def test_get_agency_runs(integration_db_session):
    result = AgencyRun.from_orm(
        get_agency_runs(PaginationParams(limit=1, offet=0), integration_db_session)[0]
    )
    assert result.agency is not None
