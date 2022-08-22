from democratizing.author_affiliations.crud import get_author_affiliations
from democratizing.schemas import AuthorAffiliation
from democratizing.dependencies import PaginationParams


def test_get_author_affiliations(integration_db_session):
    result = AuthorAffiliation.from_orm(
        get_author_affiliations(
            PaginationParams(limit=1, offet=0), integration_db_session
        )[0]
    )
    assert result.publication_author_id is not None
