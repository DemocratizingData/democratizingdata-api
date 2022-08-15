from democratizing.models import DatasetAlias


def test_datasets(test_client, mock_db):
    mock_db.query.return_value.all.return_value = [
        DatasetAlias(id=1, alias="test") 
    ]
    response = test_client.get("/dataset_aliases")
    assert response.status_code == 200
    result = response.json()
    assert result[0]["alias"] == "test"
