from typing import List

import tibiapi.tools.strainer as strainer
from tibiapi.endpoints.characters.enums import CharacterPageIdentifiers
from tibiapi.endpoints.characters.schemas import Achievements, Badges, Character
from tibiapi.gateway import client


async def get_character(character_name: str) -> Character:
    """
    Get a character by his name.
    Scrape the Tibia.com website to get the character's information.
    """

    # section_mappers: Dict[str, Callable[[ResultSet, Character], Character]] = {
    #     'Account Badges': extract_badges,
    #     # 'Account Information': extract_information,
    #     # 'Account Achievements': extract_achievements,
    # }

    page = await client.get_character(character_name)
    page_tables = page.find_all(
        "table", {"class": CharacterPageIdentifiers.TABLE_CONTENT.value})

    return Character(**strainer.extract_basic_information(page_tables))
    # for section_title in page.select(f".{CharacterPageIdentifiers.SECTION_TITLE.value}"):
    #     if (extractor := section_mappers.get(section_title.text)):
    #         extractor(page_tables, character)

    # return character


async def get_achievements(character_name: str) -> List[Achievements]:
    """
    Get achievements from a character.
    Scrape the Tibia.com website to get the character's achievements.
    """
    page = await client.get_character(character_name)
    page_tables = page.find_all(
        "table", {"class": CharacterPageIdentifiers.TABLE_CONTENT.value})

    return strainer.extract_achievements(page_tables)
