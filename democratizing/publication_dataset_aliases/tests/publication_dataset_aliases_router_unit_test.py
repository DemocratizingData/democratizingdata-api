from democratizing.models import PublicationDatasetAlias


def test_publication_dataset_aliases(test_client, mock_db):
    mock_db.query.return_value.all.return_value = [
        PublicationDatasetAlias(id=1, publication_id=1)
    ]
    response = test_client.get("/publication_dataset_aliases")
    assert response.status_code == 200
    result = response.json()
    assert result[0]["publication_id"] == 1
