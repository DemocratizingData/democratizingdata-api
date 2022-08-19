from democratizing.models import ISSN
import logging


def test_authors(test_client, mock_db):
    mock_db.query.return_value.all.return_value = [ISSN(id=1, ISSN="test")]
    response = test_client.get("/issns")
    assert response.status_code == 200
    result = response.json()
    assert result[0]["ISSN"] == "test"
