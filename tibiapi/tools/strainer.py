from typing import Dict, List

from bs4 import ResultSet

from tibiapi.endpoints.characters.enums import CharacterPageIdentifiers
from tibiapi.endpoints.characters.schemas import Achievements, Badges, Character
from tibiapi.tools import extract_table_information


def extract_basic_information(content: ResultSet) -> Dict[str, str]:
    """
    Extract basic information from the character's page, the
    basic information are name, sex, vocation and etc.
    """

    char_info_table = content[0]
    return extract_table_information(char_info_table)


def extract_achievements(content: ResultSet) -> List[Achievements]:
    """
    Extract achievements from the character's page.
    The third table is the achievements, some
    achievements are considered secrets and
    have a special HTML element on it.
    """

    achievements = content[1]
    rows = zip(*(iter(achievements.find_all("td")),) * 2)

    mapped_achievements = []
    breakpoint()
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
            "img", {"class": CharacterPageIdentifiers.SECRET_ACHIEVEMENT.value})

        mapped_achievements.append(Achievements(
            grade=grade, name=name_column.text, secret=len(secrets) > 0))

    return mapped_achievements


def extract_badges(content: ResultSet, char: Character) -> Character:
    """
    Extract the badge's information from character's page.
    The second table is the badges' information,
    sometimes this table is hidden in case on a
    character has no badges.
    """

    badges_table = content[1]
    badges: List[Badges] = []
    for badge in badges_table.find_all("img"):
        name, image = badge['alt'], badge['src']
        badges.append(Badges(name=name, icon_url=image))

    char.badges = badges

    return char
