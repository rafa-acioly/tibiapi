from typing import List

from . import sieve
from .client import all_worlds, get_world
from .schemas import World, WorldDetail


async def list_worlds() -> List[World]:
    """Retrieve the list of all worlds."""

    page = await all_worlds()

    breakpoint()
    worlds_table = page.select_one(".TableContent:has(tr.Even)")

    # The third table contains the list of worlds.
    # The first and second tables are the header.
    table_rows = worlds_table.select("tr:not(.LabelH)")

    worlds: List[World] = []

    # Skip the first row, which is the header.
    for row in table_rows:
        cells = row.find_all("td")
        additional_info = cells[5].text.split(",") if len(cells[5].text) > 0 else []
        additional_information = [info.strip() for info in additional_info]

        worlds.append(
            World(
                name=cells[0].find("a").text,
                players_online=int(cells[1].text),
                location=cells[2].text,
                pvp_type=cells[3].text,
                additional_information=additional_information,
            )
        )

    return worlds


async def find_world(world_name: str) -> WorldDetail:
    """Find a world by its name."""

    page = await get_world(world_name)

    world_table = page.select(".TableContainer table")[2].find("table")

    return sieve.extract_world_detail(world_table)
