from democratizing.models import PublicationAffiliation
import logging


def test_publication_affiliation(test_client, mock_db):
    mock_db.query.return_value.all.return_value = [
        PublicationAffiliation(id=1, institution_name="test")
    ]
    response = test_client.get("/publication_affiliations")
    assert response.status_code == 200
    result = response.json()
    assert result[0]["institution_name"] == "test"
