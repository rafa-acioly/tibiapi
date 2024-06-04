import pytest
from fastapi.testclient import TestClient
from vcr import use_cassette

from tibiapi.main import app

client = TestClient(app)


@pytest.mark.vcr()
def test_get_worlds():
    response = client.get("/api/v1/worlds")
    assert response.status_code == 200

    data = response.json()

    assert len(data) != 0


@pytest.mark.vcr()
def test_get_world():
    response = client.get("/api/v1/worlds/Antica")
    assert response.status_code == 200

    data = response.json()

    assert data["players_online"] != 0
    assert data["location"] == "Europe"
