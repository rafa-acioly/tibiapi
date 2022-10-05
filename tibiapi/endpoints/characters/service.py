from typing import Callable, Dict, List

from bs4 import ResultSet
from tibiapi.endpoints.characters.enums import CharacterPageIdentifiers
from tibiapi.endpoints.characters.schemas import Achievements, Badges, Character
from tibiapi.gateway import client
from tibiapi.tools import extract_table_information


async def get_character(character_name: str) -> Character:
    """
    Get a character by his name.
    Scrape the Tibia.com website to get the character's information.
    """

    section_mappers: Dict[str, Callable] = {
        'Account Badges': extract_badges,
        'Account Information': extract_information,
        'Account Achievements': extract_achievements,
    }

    page = await client.get_character(character_name)
    page_tables = page.find_all(
        "table", {"class": CharacterPageIdentifiers.TABLE_CONTENT.value})

    character = Character(**extract_basic_information(page_tables))
    for section_title in page.select(f".{CharacterPageIdentifiers.SECTION_TITLE.value}"):
        if (extractor := section_mappers.get(section_title)):
            extractor(page_tables, character)

    return character

    # char_info = extract_basic_information(page_tables)
    # char_achievements = extract_achievements(page_tables)
    # char_information = extract_information(page_tables)

    # return char_info | char_achievements


def extract_basic_information(content: ResultSet) -> Dict[str, str]:
    """
    Extract basic information from the character's page, the
    basic information are name, sex, vocation and etc.
    """

    char_info_table = content[0]
    return extract_table_information(char_info_table)


def extract_badges(content: ResultSet, char: Character) -> List[Badges]:
    """
    Extract the badge's information from character's page.
    The second table is the badges' information,
    sometimes this table is hidden in case on a
    character has no badges.
    """

    return []


def extract_achievements(content: ResultSet, char: Character) -> Character:
    """
    Extract achievements from the character's page.
    The third table is the achievements, some
    achievements are considered secrets and
    have a special HTML element on it.
    """

    achievements = content[2]
    rows = zip(*(iter(achievements.find_all("td")),) * 2)

    mapped_achievements = []
    for row in rows:
        grade_column, name_column = row

        # Every grade column contains "N" HTML elements with
        # a "star" icon, the amount of stars tells the
        # grade of the achievements.
        grade = len(grade_column.findChildren())

        # If the achievement is a "secret" achievement,
        # the column with the name will have an HTML
        # child with a tag "secret".
        secrets = name_column.findChildren(
            "img", {"class": CharacterPageIdentifiers.SECRET_ACHIEVEMENT})

        mapped_achievements.append(Achievements(
            grade=grade, name=name_column.text, secret=len(secrets) > 0))

    char.achievements = mapped_achievements

    return char


def extract_deaths():
    pass


def extract_guild():
    pass


def extract_information(content: ResultSet, char: Character) -> Character:
    """
    Extract acccount information from the character's page.
    The fourth table is the account information.
    """
    achievements = content[3]

    char.information = extract_table_information(achievements)

    return char
