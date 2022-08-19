from democratizing.models import Publisher
import logging


def test_publishers(test_client, mock_db):
    mock_db.query.return_value.all.return_value = [Publisher(id=1, name="test")]
    response = test_client.get("/publishers")
    assert response.status_code == 200
    result = response.json()
    assert result[0]["name"] == "test"
