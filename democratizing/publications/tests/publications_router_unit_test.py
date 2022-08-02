from democratizing.models import Publication


def test_publications(test_client, mock_db):
    mock_db.query.return_value.all.return_value = [
        Publication(id=1, run_id=1, title="test")
    ]
    response = test_client.get("/publications")
    assert response.status_code == 200
    result = response.json()
    assert result[0]["title"] == "test"
