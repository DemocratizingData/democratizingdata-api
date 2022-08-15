from democratizing.models import Model


def test_models(test_client, mock_db):
    mock_db.query.return_value.all.return_value = [
        Model(
            id=1,
            name="test",
            github_commit_url="https://github.com/",
            description="test description",
        )
    ]
    response = test_client.get("/models")
    assert response.status_code == 200
    mock_db.query.assert_called_with(Model)
    result = response.json()
    assert result[0]["name"] == "test"
