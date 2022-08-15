from unittest.mock import MagicMock

def test_datasets(test_client, mock_db):
    mock_db.query.return_value.all.return_value = [MagicMock(id=1, alias="test")]
    response = test_client.get("/datasets")
    assert response.status_code == 200

