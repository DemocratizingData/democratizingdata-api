from democratizing.topics.crud import get_topics, get_topic_publications
from democratizing.schemas import Topic, Publication
from democratizing.dependencies import PaginationParams


def test_get_topics(integration_db_session):
    result = Topic.from_orm(
        get_topics(PaginationParams(limit=1, offset=0), integration_db_session)[0]
    )
    assert result.id is not None


def test_get_topic_publications(integration_db_session):
    result = Publication.from_orm(
        get_topic_publications(
            1, PaginationParams(limit=1, offset=0), integration_db_session
        )[0]
    )
    assert result.id is not None
