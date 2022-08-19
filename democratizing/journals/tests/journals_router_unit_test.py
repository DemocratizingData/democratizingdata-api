from democratizing.models import Journal
import logging


def test_publishers(test_client, mock_db):
    mock_db.query.return_value.all.return_value = [Journal(id=1, title="test")]
    response = test_client.get("/journals")
    assert response.status_code == 200
    result = response.json()
    assert result[0]["title"] == "test"
