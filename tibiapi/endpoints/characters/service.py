from collections import defaultdict

import httpx
from bs4 import BeautifulSoup
from decouple import config

from .schemas import Character

URL = config("CHARACTERS_URL")


async def get_character(character_name: str) -> Character:
    """
    Get a character by his name.
    Scrape the Tibia.com website to get the character's information.
    """

    full_url = URL.format(character_name)

    with httpx.AsyncClient() as client:
        response = await client.get(full_url)
        soup = BeautifulSoup(response.content, "html.parser")

        informations = soup.find("table", {"class": "TableContent"})

        content = defaultdict(str)
        for table in informations:
            for column in table.find_all("td"):
                content[column.text] = column.next_sibling.text

        return Character(**content)

