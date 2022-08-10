from democratizing.topics.crud import get_topics
from democratizing.schemas import Topic


def test_get_topics(integration_db_session, topic_schema):
    result = Topic.from_orm(get_topics(1, 0, integration_db_session)[0])
    assert result == topic_schema
