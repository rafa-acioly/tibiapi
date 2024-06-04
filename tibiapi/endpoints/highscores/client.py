from urllib.parse import urlparse

from bs4 import BeautifulSoup

from tibiapi.gateway.client import get_page, post_on_page

from .enums import HighScoreCategory, HighScoreVocation, HighScoreWorld

HIGHSCORE_URL = "https://www.tibia.com/community/?subtopic=highscores"


async def get_highscore() -> BeautifulSoup:
    """Retrieve the highscore page by its parameters."""

    response = await get_page(HIGHSCORE_URL)
    response.raise_for_status()

    page = BeautifulSoup(response.content, "html.parser")

    return page


async def retrieve_highscores(query: dict[str, str | int]) -> BeautifulSoup:
    """Retrieve the highscores page by its parameters."""

    response = await post_on_page(HIGHSCORE_URL, query)
    response.raise_for_status()

    page = BeautifulSoup(response.content, "html.parser")

    return page
