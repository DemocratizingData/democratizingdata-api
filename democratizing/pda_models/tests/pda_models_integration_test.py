from democratizing.pda_models.crud import (
    get_pda_models,
)
from democratizing.schemas import PdaModels
from democratizing.dependencies import PaginationParams


def test_get_pda_models(integration_db_session):
    result = PdaModels.from_orm(
        get_pda_models(PaginationParams(limit=1, offet=0), integration_db_session)[0]
    )
    assert result.model_id is not None
