from democratizing.publication_dataset_aliases.crud import (
    get_publication_dataset_aliases,
)
from democratizing.schemas import PublicationDatasetAlias
from democratizing.dependencies import PaginationParams


def test_get_publication_dataset_aliases(integration_db_session):
    result = PublicationDatasetAlias.from_orm(
        get_publication_dataset_aliases(
            PaginationParams(limit=1, offet=0), integration_db_session
        )[0]
    )
    assert result.publication_id is not None
