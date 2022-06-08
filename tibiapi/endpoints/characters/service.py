from decouple import config
from bs4 import BeautifulSoup
import httpx


URL = config("CHARACTERS_URL")


async def get_character(character_name: str):
    full_url = URL.format(character_name)
    with httpx.AsyncClient() as client:
        response = await client.get(full_url)
        soup = BeautifulSoup(response.content, "html.parser")
        pass