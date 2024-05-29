from typing import List

import tibiapi.tools.strainer as strainer
from tibiapi.endpoints.characters.enums import CharacterPageIdentifiers
from tibiapi.endpoints.characters.schemas import Achievements, Character, Characters
from tibiapi.gateway import client


async def get_character(character_name: str) -> Character:
    """
    Get a character by his name.
    Scrape the Tibia.com website to get the character's information.
    """
    page = await client.get_character(character_name)
    page_tables = page.find_all(
        "table", {"class": CharacterPageIdentifiers.TABLE_CONTENT.value})

    return strainer.extract_basic_information(page_tables)


async def get_characters(character_name: str):
    """
    Get a list of all characters from a specific player.
    Scrape the Tibia.com website to get the character's information.
    """
    page = await client.get_character(character_name)
    page_tables = page.find_all(
        "table", {"class": CharacterPageIdentifiers.TABLE_CONTENT.value})

    return strainer.extract_characters(page_tables)


async def get_achievements(character_name: str) -> List[Achievements]:
    """
    Get achievements from a character.
    Scrape the Tibia.com website to get the character's achievements.
    """
    page = await client.get_character(character_name)
    page_tables = page.find_all(
        "table", {"class": CharacterPageIdentifiers.TABLE_CONTENT.value})

    return strainer.extract_achievements(page_tables)
