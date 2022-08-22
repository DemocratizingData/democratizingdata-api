from democratizing.models import Asjc
import logging


def test_authors(test_client, mock_db):
    mock_db.query.return_value.all.return_value = [Asjc(id=1, label="test")]
    response = test_client.get("/asjcs")
    assert response.status_code == 200
    result = response.json()
    assert result[0]["label"] == "test"
