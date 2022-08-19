from democratizing.models import AuthorAffiliation
import logging


def test_author_affiliations(test_client, mock_db):
    mock_db.query.return_value.all.return_value = [
        AuthorAffiliation(id=1, publication_author_id=1)
    ]
    response = test_client.get("/author_affiliations")
    assert response.status_code == 200
    result = response.json()
    assert result[0]["publication_author_id"] == 1
