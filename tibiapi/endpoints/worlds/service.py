from typing import List

from . import sieve
from .client import all_worlds, get_world
from .schemas import World, WorldDetail


async def list_worlds() -> List[World]:
    """Retrieve the list of all worlds."""

    page = await all_worlds()

    worlds_table = page.select(".TableContent")

    # The third table contains the list of worlds.
    # The first and second tables are the header.
    table_rows = worlds_table[2].select("tr")

    worlds: List[World] = []

    # Skip the first row, which is the header.
    for row in table_rows[1:]:
        cells = row.find_all("td")

        worlds.append(World(
            name=cells[0].find("a").text,
            players_online=int(cells[1].text),
            location=cells[2].text,
            pvp_type=cells[3].text,
            additional_information=cells[5].text if len(
                cells[5].text) > 0 else None
        ))

    return worlds


async def find_world(world_name: str) -> WorldDetail:
    """Find a world by its name."""

    page = await get_world(world_name)

    world_table = page.select(".TableContainer table")[2].find("table")

    return sieve.extract_world_detail(world_table)
