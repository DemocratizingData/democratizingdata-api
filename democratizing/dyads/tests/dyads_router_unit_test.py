from democratizing.models import Dyad


def test_dyads(test_client, mock_db):
    mock_db.query.return_value.all.return_value = [
        Dyad(id=1, publication_id=1)
    ]
    response = test_client.get("/dyads")
    assert response.status_code == 200
    result = response.json()
    assert result[0]["publication_id"] == 1
