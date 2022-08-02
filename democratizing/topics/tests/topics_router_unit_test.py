from democratizing.models import Topic


def test_topics(test_client, mock_db):
    mock_db.query.return_value.all.return_value = [
        Topic(id=1, run_id=1, keywords="test")
    ]
    response = test_client.get("/topics")
    assert response.status_code == 200
    result = response.json()
    assert result[0]["keywords"] == "test"
