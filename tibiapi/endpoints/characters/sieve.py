from typing import List

from bs4 import ResultSet

from tibiapi.tools.sieve import extract_table_information

from .enums import CharacterPageIdentifiers
from .schemas import Achievements, Character, Characters


def extract_basic_information(content: ResultSet) -> Character:
    """
    Extract basic information from the character's page, the
    basic information are name, sex, vocation and etc.
    """

    char_info_table = content[0]
    account_info_table = content[2]

    char_info = extract_table_information(char_info_table)
    account_info = extract_table_information(account_info_table)

    char = char_info | account_info

    return Character(**char)


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


def extract_characters(content: ResultSet) -> List[Characters]:
    """
    Extract a list of characters from the player's page.
    The second to last table is the list of
    characters from the player.
    """

    # Although the website shows the table as the second to last,
    # the table is the forth from last in the HTML content.
    # The last tables (after the fourth) are the footer of the page,
    # and the cookies disclaimer.
    characters_table = content[len(content) - 4]
    characters: List[Characters] = []

    # Ignore the first row of the table, this row contains the table headers.
    for char in characters_table.find_all("tr")[1:]:
        # The "_" variable is used to ignore the last column
        # of the table, this column is a button to view
        # the character's information.
        name_column, world_column, status_column, _ = char.find_all("td")

        # The name column contains the character's name and a number
        # example: "1. Name", we split the string by the first space
        # to get only the name.
        name = name_column.text.split(" ", 1)[1].strip()

        status = status_column.text if len(status_column.text) > 0 else None

        # The name column contains an image with an "m" letter
        # that represents the main character of the player.
        main = name_column.find("img") is not None

        characters.append(Characters(
            name=name, world=world_column.text, main=main, status=status))

    return characters
