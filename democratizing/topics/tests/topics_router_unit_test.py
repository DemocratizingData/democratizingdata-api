from democratizing.models import PublicationTopic, Topic


def test_topics(test_client, mock_db):
    mock_db.query.return_value.all.return_value = [
        Topic(id=1, run_id=1, keywords="test")
    ]
    response = test_client.get("/topics")
    assert response.status_code == 200
    mock_db.query.assert_called_with(Topic)
    result = response.json()
    assert result[0]["keywords"] == "test"


def test_topic_publications(test_client, mock_db, mock_publication_model):
    mock_db.query.return_value.join.return_value.filter.return_value.all.return_value = [
        mock_publication_model
    ]
    response = test_client.get("/topics/1/publications")
    called_expression = mock_db.query.return_value.join.return_value.filter.mock_calls[
        0
    ].args[0]
    assert called_expression.compare(PublicationTopic.topic_id == 1)
    assert response.status_code == 200
    result = response.json()
    assert result[0]["id"] == 61
