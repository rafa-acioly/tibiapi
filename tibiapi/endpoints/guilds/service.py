import re as regex
from typing import Dict, List

from tibiapi.gateway import client
from tibiapi.tools import slugify

from .schemas import Guild, GuildHall


async def find_guild(guild_name: str) -> Guild:
    """
    Get a guild by its name.
    The guild information is scraped from the Tibia.com website.

    The HTML element that contains the guild information contains
    the following structure:

    <div id="GuildInformationContainer">
        We took over this ship. <br><br>
        The guild was founded on {{ server }} on {{ date }}.<br>
        It is currently {{ status }}.<br>
        Guild is opened for applications.<br>
        The official homepage is at {{ link }}.<br>
        Their home on {{ server }} is {{ guild_hall }}. The rent is paid until {{ date }}<br>
    </div>

    The guild information is split by new lines and the information is
    extracted from the text.
    """
    page = await client.get_guild(guild_name)

    guild_info_container = page.select_one("#GuildInformationContainer")
    guild_paragraphs = guild_info_container.text.split("\n")

    world, foundation_date = _parse_guild_foundation(guild_paragraphs)

    return Guild(
        name=guild_name,
        world=world,
        active=_parse_guild_status(guild_paragraphs),
        open_applications=_parse_guild_application(guild_paragraphs),
        guild_hall=_parse_guild_hall(guild_paragraphs),
        foundation_date=foundation_date,
        homepage=_parse_guild_homepage(guild_paragraphs),
    )


def _parse_guild_foundation(paragraphs: List[str]) -> Dict[str, str]:
    """
    Parse the foundation date from the guild information.

    The foundation date is in the following format:
    "The guild was founded on {{ server }} on {{ date }}."
    """

    for paragraph in paragraphs:
        if paragraph.startswith("The guild was founded"):
            pattern = r"on (\w+) on (.+)\."
            match = regex.search(pattern, paragraph)

            return {"world": match.group(1), "foundation_date": match.group(2)}


def _parse_guild_hall(paragraphs: List[str]) -> GuildHall:
    """
    Parse the guild hall information from the guild information.
    The guild hall information contains the world, the name of the guild hall,
    and the date until the rent is paid.

    The guild hall information is in the following format:
    "Their home on {{ server }} is {{ guild_hall }}. The rent is paid until {{ date }}"
    """

    for paragraph in paragraphs:
        if paragraph.startswith("Their home"):
            pattern = r"is ([^.]+)\. .* until (.+)\.$"
            match = regex.search(pattern, paragraph)

            return GuildHall(name=match.group(1), paid_until=match.group(2))

    return GuildHall()


def _parse_guild_status(paragraphs: List[str]) -> bool:
    """
    Parse the guild status from the guild information.

    The guild status is in the following format:
    "It is currently {{ status }}."
    """

    for paragraph in paragraphs:
        if paragraph.startswith("It is currently"):
            return "active" in paragraph

    return False


def _parse_guild_application(paragraphs: List[str]) -> bool:
    """
    Parse the guild application status from the guild information.

    The guild application status is in the following format:
    "Guild is opened for applications."
    """

    for paragraph in paragraphs:
        if paragraph.startswith("Guild is") and "opened" in paragraph:
            return True

    return False


def _parse_guild_homepage(paragraphs: List[str]) -> str:
    """
    Parse the guild homepage from the guild information.

    The guild homepage is in the following format:
    "The official homepage is at {{ link }}."
    """

    for paragraph in paragraphs:
        if paragraph.startswith("The official homepage"):
            pattern = r"at (.+)\.$"
            match = regex.search(pattern, paragraph)

            return match.group(1)

    return None
