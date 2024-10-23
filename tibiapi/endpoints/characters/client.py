from bs4 import BeautifulSoup
from fastapi_redis_cache import cache_one_hour

from tibiapi.gateway.client import get_page

from .exceptions import CharacterNotFound

CHARACTER_URL = "https://www.tibia.com/community/?subtopic=characters&name={name}"


@cache_one_hour()
async def get_character(name: str) -> BeautifulSoup:
    """Retrieve the character page by its name."""

    response = await get_page(CHARACTER_URL.format(name=name))
    response.raise_for_status()

    page = BeautifulSoup(response.content, "html.parser")

    has_not_found_text = page.find("div", string="Could not find character") is not None
    if has_not_found_text:
        raise CharacterNotFound(name)

    return page
