from democratizing.topics.crud import get_topics, get_topic_publications
from democratizing.schemas import Topic, Publication


def test_get_topics(integration_db_session, topic_schema):
    result = Topic.from_orm(get_topics(1, 0, integration_db_session)[0])
    assert result == topic_schema


def test_get_topic_publications(integration_db_session, topic_schema):
    result = Publication.from_orm(
        get_topic_publications(1, 1, 0, integration_db_session)[0]
    )
    assert result.id is not None
