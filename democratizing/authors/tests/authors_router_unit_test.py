from democratizing.models import Author


def test_authors(test_client, mock_db):
    mock_db.query.return_value.all.return_value = [
        Author(id=1, given_name="test", family_name="author")
    ]
    response = test_client.get("/authors")
    assert response.status_code == 200
    result = response.json()
    assert result[0]["given_name"] == "test"
