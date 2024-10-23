from tibiapi.endpoints.worlds.enums import World

from . import sieve
from .client import get_highscore, retrieve_highscores
from .enums import HighScoreCategory, HighScoreVocation
from .schemas import HighScoreEntry


async def find_highscores(
    world_name: World = None,
    vocation: HighScoreVocation = HighScoreVocation.NONE,
    category: HighScoreCategory = None,
) -> list[HighScoreEntry]:
    """
    Retrieve the highscores page by its parameters.
    """

    query = {
        "world": world_name.title() if world_name else None,
        "profession": HighScoreVocation.numericOf(vocation),
        "category": HighScoreCategory.numericOf(category),
    }

    if any(query.values()):
        page = await retrieve_highscores(query)
    else:
        page = await get_highscore()

    table_rows = page.select("tr:has(a[href*='subtopic=characters&name'])")

    return sieve.extract_players_highscore(category, table_rows)
