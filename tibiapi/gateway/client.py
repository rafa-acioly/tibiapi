import httpx
from bs4 import BeautifulSoup


async def _get(url: str) -> BeautifulSoup:
    """
    Retrieve the page HTML content the for given URL
    """
    async with httpx.AsyncClient() as client:
        return await client.get(url)


async def _post(url: str, params: dict) -> BeautifulSoup:
    """
    Some pages require POST parameters to be sent in order to be accessed.
    """
    async with httpx.AsyncClient() as client:
        return await client.post(url=url, params=params)


async def get_character(name: str) -> BeautifulSoup:
    URL = f"https://www.tibia.com/community/?name={name}"
    response = await _get(URL)
    response.raise_for_status()

    return BeautifulSoup(response.content, "html.parser")


async def get_world(name: str) -> BeautifulSoup:
    URL = f"https://www.tibia.com/community/?subtopic=worlds&world={name}"
    response = await _get(URL)
    response.raise_for_status()

    return BeautifulSoup(response.content, "html.parser")


async def get_guild(name: str) -> BeautifulSoup:
    URL = f"https://www.tibia.com/community/?subtopic=guilds&page=view"
    response = await _post(URL, {"GuildName": name})
    response.raise_for_status()

    return BeautifulSoup(response.content, "html.parser")
