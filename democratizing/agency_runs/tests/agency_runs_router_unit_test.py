from democratizing.models import AgencyRun


def test_datasets(test_client, mock_db):
    mock_db.query.return_value.all.return_value = [AgencyRun(id=1, agency="test")]
    response = test_client.get("/agency_runs")
    assert response.status_code == 200
    result = response.json()
    assert result[0]["agency"] == "test"
