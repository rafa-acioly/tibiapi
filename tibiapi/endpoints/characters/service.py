from collections import defaultdict

from bs4 import ResultSet

from tibiapi.gateway import client
from tibiapi.tools import build_data


async def get_character(character_name: str) -> dict:
    """
    Get a character by his name.
    Scrape the Tibia.com website to get the character's information.
    """
    page = await client.get_character(character_name)

    page_tables = page.find_all("table", {"class": "TableContent"})

    char_info = extract_basic_information(page_tables)
    char_achievements = extract_achievements(page_tables)
    char_information = extract_information(page_tables)

    return char_info | char_information | char_achievements


def extract_basic_information(content: ResultSet) -> dict:
    """
    Extract basic information from the character's page.
    The first table is the basic information.
    """

    char_info_table = content[0]
    return build_data(char_info_table)


def extract_badges():
    pass


def extract_achievements(content: ResultSet) -> dict:
    """
    Extract achievements from the character's page.
    The third table is the achievements.
    """

    achievements = content[2]
    rows = zip(*(iter(achievements.find_all("td")),) * 2)
    mapped_content = {"achievements": []}
    for row in rows:
        grade_column, name_column = row

        # Every grade column contains "N" HTML icon that represents the grade.
        grade = len(grade_column.findChildren())
        # If the column name contains a secret achievement, it will be marked as such.
        secret = name_column.findChildren(
            "img", {"class": "SecretAchievementIcon"})

        mapped_content["achievements"].append({
            "grade": grade,
            "name": name_column.text,
            "secret": len(secret) > 0
        })

    return mapped_content


def extract_deaths():
    pass


def extract_guild():
    pass


def extract_information(content: ResultSet) -> dict:
    """
    Extract acccount information from the character's page.
    The fourth table is the account information.
    """
    achievements = content[3]

    return {"information": build_data(achievements)}
