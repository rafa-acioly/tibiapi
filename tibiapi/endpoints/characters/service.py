from collections import defaultdict

import httpx
from bs4 import BeautifulSoup, Tag

from tibiapi.tools import slugify

URL = "https://www.tibia.com/community/?name={name}"


async def get_character(character_name: str) -> dict:
    """
    Get a character by his name.
    Scrape the Tibia.com website to get the character's information.
    """

    full_url = URL.format(name=character_name)

    async with httpx.AsyncClient() as client:
        response = await client.get(full_url)
        soup = BeautifulSoup(response.content, "html.parser")

        informations = soup.find_all("table", {"class": "TableContent"})

        char_info = extract_basic_information(informations)
        char_achievements = extract_achievements(informations)

        return char_info | char_achievements


def extract_basic_information(content: Tag) -> dict:
    """
    Extract basic information from the character's page.
    The first table is the basic information.
    """
    char_info_table = content[0]
    return build_data(char_info_table)


def extract_badges():
    pass


def extract_achievements(content: Tag) -> dict:
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
        secret = name_column.findChildren("img", {"class": "SecretAchievementIcon"})

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


def build_data(content: list) -> dict:
    rows = zip(*(iter(content.find_all("td")),) * 2)
    mapped_content = defaultdict(str)
    for row in rows:
        column_name, column_value = row
        mapped_content[slugify(column_name.text)] = column_value.text

    return mapped_content
