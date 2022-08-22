from democratizing.models import Affiliation
import logging


def test_affiliations(test_client, mock_db):
    mock_db.query.return_value.all.return_value = [
        Affiliation(id=1, institution_name="test")
    ]
    response = test_client.get("/affiliations")
    assert response.status_code == 200
    result = response.json()
    assert result[0]["institution_name"] == "test"
