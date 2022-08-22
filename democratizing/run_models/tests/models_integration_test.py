from democratizing.run_models.crud import get_models
from democratizing.schemas import Model
from democratizing.dependencies import PaginationParams


def test_get_models(integration_db_session):
    result = Model.from_orm(
        get_models(PaginationParams(limit=1, offset=0), integration_db_session)[0]
    )
    assert result.name is not None
