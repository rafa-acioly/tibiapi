import pytest
from fastapi.testclient import TestClient

from tibiapi.endpoints.highscores.enums import HighScoreCategory
from tibiapi.main import app

client = TestClient(app)


@pytest.mark.vcr()
def test_get_highscores():
    response = client.get("/api/v1/highscores")
    assert response.status_code == 200

    data = response.json()

    assert len(data) != 0


@pytest.mark.vcr()
def test_get_highscores_by_world():
    response = client.get("/api/v1/highscores?world_name=Antica")
    assert response.status_code == 200

    data = response.json()

    assert len(data) != 0
    assert all(entry["world"] == "Antica" for entry in data)


@pytest.mark.vcr()
@pytest.mark.parametrize("query,expected_vocation", [
    ("KNIGHTS", "Knight"),
    ("PALADINS", "Paladin"),
    ("SORCERERS", "Sorcerer"),
    ("DRUIDS", "Druid")
])
def test_get_highscores_by_vocation(query: str, expected_vocation: str):
    response = client.get(f"/api/v1/highscores?vocation={query}")
    assert response.status_code == 200

    data = response.json()

    assert len(data) != 0
    assert all(expected_vocation in entry["vocation"] for entry in data)


@pytest.mark.vcr()
@pytest.mark.parametrize("skill", [category.name for category in list(HighScoreCategory)])
def test_get_highscores_by_category(skill: str):
    response = client.get(f"/api/v1/highscores?category={skill}")
    assert response.status_code == 200

    data = response.json()

    assert len(data) != 0
