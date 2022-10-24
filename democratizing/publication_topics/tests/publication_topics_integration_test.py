from democratizing.publication_topics.crud import get_publication_topics
from democratizing.schemas import PublicationTopic
from democratizing.dependencies import PaginationParams


def test_get_publication_authors(integration_db_session):
    result = PublicationTopic.from_orm(
        get_publication_topics(
            PaginationParams(limit=1, offet=0), integration_db_session
        )[0]
    )
    assert result.publication_id is not None
