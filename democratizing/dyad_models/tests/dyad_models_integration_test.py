from democratizing.dyad_models.crud import (
    get_dyad_models,
)
from democratizing.schemas import DyadModel
from democratizing.dependencies import PaginationParams


def test_get_dyad_models(integration_db_session):
    result = DyadModel.from_orm(
        get_dyad_models(PaginationParams(limit=1, offet=0), integration_db_session)[0]
    )
    assert result.model_id is not None
