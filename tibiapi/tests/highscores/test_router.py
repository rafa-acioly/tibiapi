import pytest
from fastapi.testclient import TestClient

from tibiapi.endpoints.highscores.enums import HighScoreCategory
from tibiapi.endpoints.worlds.enums import World
from tibiapi.main import app

client = TestClient(app)


@pytest.mark.vcr()
def test_get_highscores():
    response = client.get("/api/v1/highscores")
    assert response.status_code == 200

    data = response.json()

    assert len(data) != 0


@pytest.mark.vcr()
@pytest.mark.parametrize("world", [world.value for world in list(World)])
def test_get_highscores_by_world(world: str):
    response = client.get("/api/v1/highscores", params={"world_name": world})
    assert response.status_code == 200

    data = response.json()

    assert len(data) != 0
    assert all(entry["world"] == world for entry in data)


@pytest.mark.vcr()
@pytest.mark.parametrize("param", ["Knight", "Paladin", "Sorcerer", "Druid"])
def test_get_highscores_by_vocation(param: str):
    response = client.get(url="/api/v1/highscores", params={"vocation": param})
    assert response.status_code == 200

    data = response.json()

    assert len(data) != 0
    assert all(param in entry["vocation"] for entry in data)


@pytest.mark.vcr()
@pytest.mark.parametrize("skill", [category.value for category in list(HighScoreCategory)])
def test_get_highscores_by_category(skill: str):
    response = client.get(url="/api/v1/highscores", params={"category": skill})
    assert response.status_code == 200

    data = response.json()

    assert len(data) != 0
