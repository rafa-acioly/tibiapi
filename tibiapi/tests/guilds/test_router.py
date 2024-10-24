import pytest
from fastapi.testclient import TestClient
from vcr import use_cassette

from tibiapi.main import app

client = TestClient(app)


@pytest.mark.vcr()
def test_get_guild():
    response = client.get("/api/v1/guilds/Above")
    assert response.status_code == 200

    data = response.json()

    assert data["name"] == "Above"
    assert data["world"] == "Antica"
    assert data["active"] == True


@pytest.mark.vcr()
def test_get_guild_not_found():
    response = client.get("/api/v1/guilds/NotAValidGuild")

    assert response.status_code == 404
    assert response.json() == {"detail": "guild NotAValidGuild not found."}


@pytest.mark.vcr()
def test_get_guild_members():
    response = client.get("/api/v1/guilds/Above/members")
    assert response.status_code == 200

    data = response.json()

    assert len(data) != 0


@pytest.mark.vcr()
def test_get_guild_members_not_found():
    response = client.get("/api/v1/guilds/NotAValidGuild/members")

    assert response.status_code == 404
    assert response.json() == {"detail": "guild NotAValidGuild not found."}


@pytest.mark.vcr()
def test_get_guild_members_invites():
    response = client.get("/api/v1/guilds/Above/members/invites")
    assert response.status_code == 200

    data = response.json()

    assert len(data) == 0


@pytest.mark.vcr()
def test_get_guild_members_invites_not_found():
    response = client.get("/api/v1/guilds/NotAValidGuild/members/invites")

    assert response.status_code == 404
    assert response.json() == {"detail": "guild NotAValidGuild not found."}


@pytest.mark.vcr()
def test_get_guild_members_empty():
    response = client.get("/api/v1/guilds/Forgotten Hunters/members/invites")
    assert response.status_code == 200

    data = response.json()

    assert len(data) == 0
