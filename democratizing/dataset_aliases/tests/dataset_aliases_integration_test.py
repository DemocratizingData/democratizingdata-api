from democratizing.dataset_aliases.crud import get_dataset_aliases
from democratizing.schemas import DatasetAlias
from democratizing.dependencies import PaginationParams


def test_get_datasets(integration_db_session):
    result = DatasetAlias.from_orm(
        get_dataset_aliases(PaginationParams(limit=1, offet=0), integration_db_session)[0]
    )
    assert result.id is not None
