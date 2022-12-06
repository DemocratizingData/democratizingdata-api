from democratizing.publication_affiliations.crud import get_publication_affiliations
from democratizing.schemas import PublicationAffiliation
from democratizing.dependencies import PaginationParams


def test_get_publication_affiliations(integration_db_session):
    result = PublicationAffiliation.from_orm(
        get_publication_affiliations(PaginationParams(limit=1, offet=0), integration_db_session)[0]
    )
    assert result.institution_name is not None
