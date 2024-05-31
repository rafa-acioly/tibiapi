import re as regex
from typing import Dict, List

from .schemas import GuildHall


def extract_guild_foundation(paragraphs: List[str]) -> Dict[str, str]:
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


def extract_guild_hall(paragraphs: List[str]) -> GuildHall:
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


def extract_guild_status(paragraphs: List[str]) -> bool:
    """
    Parse the guild status from the guild information.

    The guild status is in the following format:
    "It is currently {{ status }}."
    """

    for paragraph in paragraphs:
        if paragraph.startswith("It is currently"):
            return "active" in paragraph

    return False


def extract_guild_application(paragraphs: List[str]) -> bool:
    """
    Parse the guild application status from the guild information.

    The guild application status is in the following format:
    "Guild is opened for applications."
    """

    for paragraph in paragraphs:
        if paragraph.startswith("Guild is") and "opened" in paragraph:
            return True

    return False


def extract_guild_homepage(paragraphs: List[str]) -> str:
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
