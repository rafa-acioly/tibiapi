from typing import List

from bs4 import Tag

from . import sieve
from .client import get_character as get_character_page
from .schemas import Achievements, Character, Characters, Deaths


async def get_character(character_name: str) -> Character:
    """
    Get a character basic informatiom by his name.
    The character information is always displayed in the character's page.
    """

    section_header = await _get_page_section(
        character_name=character_name, section="Character Information"
    )

    table_conteiner = section_header.find_parent("div", class_="TableContainer")
    table_content = table_conteiner.find("table", class_="TableContent")

    return sieve.extract_basic_information(table_content)


async def get_characters(character_name: str) -> List[Characters]:
    """
    Get a list of all characters from a specific player.
    The characters list are always displayed in the character's page.
    """

    section_header = await _get_page_section(
        character_name=character_name, section="Characters"
    )

    if not section_header:
        return []

    table_conteiner = section_header.find_parent("div", class_="TableContainer")
    table_content = table_conteiner.find("table", class_="TableContent")

    return sieve.extract_characters(table_content)


async def get_achievements(character_name: str) -> List[Achievements]:
    """
    Get achievements from a character.
    The achievements is always displayed in the character's page.
    """

    section_header = await _get_page_section(
        character_name=character_name, section="Account Achievements"
    )

    if not section_header:
        return []

    table_conteiner = section_header.find_parent("div", class_="TableContainer")
    table_content = table_conteiner.find("table", class_="TableContent")

    return sieve.extract_achievements(table_content)


async def get_deaths(character_name: str) -> List[Deaths]:
    """
    Get deaths from a character.
    Scrape the Tibia.com website to get the character's deaths.
    """

    section_header = await _get_page_section(
        character_name=character_name, section="Character Deaths"
    )

    if not section_header:
        return []

    table_conteiner = section_header.find_parent("div", class_="TableContainer")
    table_content = table_conteiner.find("table", class_="TableContent")

    if not table_content:
        return []

    return sieve.extract_deaths(table_content)


async def _get_page_section(character_name: str, section: str) -> Tag | None:
    """
    Get the character's page section.
    In order to get the character's information, we need to
    get the page section where the information is located.
    When we get the page section, we can extract the information.
    """

    page = await get_character_page(character_name)
    return page.find("div", class_="Text", string=section)
