from bs4 import BeautifulSoup

from tibiapi.gateway.client import get_page

from .exceptions import GuildNotFound

GUILD_URL = "https://www.tibia.com/community/?subtopic=guilds&page=view&GuildName={guild_name}"


async def get_guild(name: str) -> BeautifulSoup:
    """Retrieve the guild page by its name."""

    response = await get_page(GUILD_URL.format(guild_name=name))
    response.raise_for_status()

    page = BeautifulSoup(response.content, "html.parser")

    has_no_guild_container = page.select_one("#GuildInformationContainer")
    if has_no_guild_container is None:
        raise GuildNotFound(name)

    return page
