from democratizing.models import PublicationAuthor


def test_publication_authors(test_client, mock_db):
    mock_db.query.return_value.all.return_value = [
        PublicationAuthor(id=1, publication_id=1)
    ]
    response = test_client.get("/publication_authors")
    assert response.status_code == 200
    result = response.json()
    assert result[0]["publication_id"] == 1
