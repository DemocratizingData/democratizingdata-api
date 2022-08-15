from democratizing.datasets.crud import get_datasets
from democratizing.schemas import Dataset
from democratizing.dependencies import PaginationParams


def test_get_datasets(integration_db_session):
    result = Dataset.from_orm(
        get_datasets(PaginationParams(limit=1, offet=0), integration_db_session)[
            0
        ]
    )
    assert result.id is not None
