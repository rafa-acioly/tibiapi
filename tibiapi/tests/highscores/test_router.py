import pytest
from fastapi.testclient import TestClient
from vcr import use_cassette

from tibiapi.main import app

client = TestClient(app)


@pytest.mark.vcr()
def test_get_highscores():
    response = client.get("/api/v1/highscores")
    assert response.status_code == 200

    data = response.json()

    assert len(data) != 0
