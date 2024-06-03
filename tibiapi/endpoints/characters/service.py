import re as regex
from typing import List

from . import sieve
from .client import get_character as get_character_page
from .enums import CharacterPageIdentifiers
from .schemas import Achievements, Character, Characters


async def get_character(character_name: str) -> Character:
    """
    Get a character by his name.
    Scrape the Tibia.com website to get the character's information.
    """

    page_tables = await _get_character_page_tables(character_name)

    return sieve.extract_basic_information(page_tables)


async def get_characters(character_name: str) -> List[Characters]:
    """
    Get a list of all characters from a specific player.
    Scrape the Tibia.com website to get the character's information.
    """

    page_tables = await _get_character_page_tables(character_name)

    return sieve.extract_characters(page_tables)


async def get_achievements(character_name: str) -> List[Achievements]:
    """
    Get achievements from a character.
    Scrape the Tibia.com website to get the character's achievements.
    """

    page_tables = await _get_character_page_tables(character_name)

    return sieve.extract_achievements(page_tables)


async def _get_character_page_tables(character_name: str):
    """
    Get the character's page tables.
    The page tables are the HTML tables that contain the character's information,
    such as achievements, deaths, etc. All tables have the same class
    name "TableContent".
    """

    page = await get_character_page(character_name)

    return page.find_all(
        "table", {"class": CharacterPageIdentifiers.TABLE_CONTENT.value})
