from bs4 import BeautifulSoup

from tibiapi.gateway.client import get_page

LIST_WORLD_URL = "https://www.tibia.com/community/?subtopic=worlds"
WORLD_URL = "https://www.tibia.com/community/?subtopic=worlds&world={name}"


async def get_world(name: str) -> BeautifulSoup:
    """Retrieve the world page by its name."""

    response = await get_page(WORLD_URL.format(name=name))
    response.raise_for_status()

    return BeautifulSoup(response.content, "html.parser")


async def all_worlds() -> BeautifulSoup:
    """Retrieve the page of list of all worlds."""

    response = await get_page(LIST_WORLD_URL)
    response.raise_for_status()

    return BeautifulSoup(response.content, "html.parser")
