import pytest
from fastapi.testclient import TestClient
from vcr import use_cassette

from tibiapi.main import app

client = TestClient(app)


@pytest.mark.vcr()
def test_get_characters():
    response = client.get("/api/v1/character/Rubini")
    assert response.status_code == 200

    data = response.json()

    assert data["name"] == "Rubini"
    assert data["level"] == 8


@pytest.mark.vcr()
def test_get_characters_not_found():
    response = client.get("/api/v1/character/NotAValidCharacter")

    assert response.status_code == 404
    assert response.json() == {
        "detail": "character NotAValidCharacter not found."}


@pytest.mark.vcr()
def test_get_characters_list():
    response = client.get("/api/v1/character/Rubini/characters")
    assert response.status_code == 200

    data = response.json()

    assert len(data) == 3


@pytest.mark.vcr()
def test_get_characters_list_not_found():
    response = client.get("/api/v1/character/NotAValidCharacter/characters")

    assert response.status_code == 404
    assert response.json() == {
        "detail": "character NotAValidCharacter not found."}


@pytest.mark.vcr()
def test_get_achievements():
    response = client.get("/api/v1/character/Rubini/achievements")
    assert response.status_code == 200

    data = response.json()

    assert len(data) == 0


@pytest.mark.vcr()
def test_get_achievements_not_found():
    response = client.get("/api/v1/character/NotAValidCharacter/achievements")

    assert response.status_code == 404
    assert response.json() == {
        "detail": "character NotAValidCharacter not found."}
