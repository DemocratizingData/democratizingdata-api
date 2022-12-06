from democratizing.models import DyadModel


def test_dyad_models(test_client, mock_db):
    mock_db.query.return_value.all.return_value = [DyadModel(id=1, model_id=1)]
    response = test_client.get("/dyad_models")
    assert response.status_code == 200
    result = response.json()
    assert result[0]["model_id"] == 1
