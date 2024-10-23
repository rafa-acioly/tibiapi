from typing import List
from bs4 import Tag

from . import sieve
from .client import get_character as get_character_page
from .schemas import Achievements, Character, Characters, Deaths


async def get_character(character_name: str) -> Character:
    """
    Get a character by his name.
    Scrape the Tibia.com website to get the character's information.
    """

    char_content = await _get_character_page_tables(
        character_name=character_name,
        section="Character Information")

    return sieve.extract_basic_information(char_content)

async def get_characters(character_name: str) -> List[Characters]:
    """
    Get a list of all characters from a specific player.
    Scrape the Tibia.com website to get the character's information.
    """

    table_content = await _get_character_page_tables(
        character_name=character_name,
        section="Characters")

    return sieve.extract_characters(table_content)

async def get_achievements(character_name: str) -> List[Achievements]:
    """
    Get achievements from a character.
    Scrape the Tibia.com website to get the character's achievements.
    """

    table_content = await _get_character_page_tables(
        character_name=character_name,
        section="Account Achievements")

    return sieve.extract_achievements(table_content)

async def get_deaths(character_name: str) -> List[Deaths]:
    """
    Get deaths from a character.
    Scrape the Tibia.com website to get the character's deaths.
    """

    table_content = await _get_character_page_tables(
        character_name=character_name,
        section="Character Deaths")

    if not table_content:
        return []

    return sieve.extract_deaths(table_content)

async def _get_character_page_tables(character_name: str, section: str) -> Tag:
    """
    Get the character's page tables.
    The page tables are the HTML tables that contain the character's information,
    such as achievements, deaths, etc. All tables have the same class
    name "TableContent".
    """

    page = await get_character_page(character_name)
    section_div = page.find("div", class_="Text", string=section)

    if not section_div:
        return None

    table_conteiner = section_div.find_parent("div", class_="TableContainer")
    table_content = table_conteiner.find("table", class_="TableContent")

    return table_content
