import httpx
from bs4 import BeautifulSoup

from tibiapi.endpoints.characters.exceptions import CharacterNotFound

CHARACTER_URL = "https://www.tibia.com/community/?subtopic=characters&name={name}"
WORLD_URL = "https://www.tibia.com/community/?subtopic=worlds&world={name}"
GUILD_URL = "https://www.tibia.com/community/?subtopic=guilds&page=view"


async def _get(url: str):
    """
    Retrieve the page HTML content the for given URL
    """
    async with httpx.AsyncClient() as client:
        return await client.get(url)


async def _post(url: str, params: dict):
    """
    Some pages require POST parameters to be sent in order to be accessed.
    """
    async with httpx.AsyncClient() as client:
        return await client.post(url=url, params=params)


async def get_character(name: str) -> BeautifulSoup:
    response = await _get(CHARACTER_URL.format(name=name))
    response.raise_for_status()

    page = BeautifulSoup(response.content, "html.parser")

    has_not_found_text = page.find(
        "div", text="Could not find character") is not None
    if has_not_found_text:
        raise CharacterNotFound(name)

    return page


async def get_world(name: str) -> BeautifulSoup:
    response = await _get(WORLD_URL.format(name=name))
    response.raise_for_status()

    return BeautifulSoup(response.content, "html.parser")


async def get_guild(name: str) -> BeautifulSoup:
    response = await _post(GUILD_URL, {"GuildName": name})
    response.raise_for_status()

    return BeautifulSoup(response.content, "html.parser")
