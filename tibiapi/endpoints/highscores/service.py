from . import sieve
from .client import get_highscore, retrieve_highscores
from .enums import HighScoreCategory, HighScoreVocation, HighScoreWorld
from .schemas import HighScoreEntry


async def find_highscores(
    world_name: HighScoreWorld = None,
    vocation: HighScoreVocation = HighScoreVocation.NONE,
    category: HighScoreCategory = None
) -> list[HighScoreEntry]:
    """
    Retrieve the highscores page by its parameters.
    """

    query = {
        "world_name": world_name.title() if world_name else None,
        "vocation": HighScoreVocation.numericOf(vocation),
        "category": HighScoreCategory.numericOf(category)
    }
    page = get_highscore() if any(query.values()) else await retrieve_highscores(query)

    table_rows = page.select(
        "tr:has(a[href*='subtopic=characters&name'])")

    return sieve.extract_players_highscore(table_rows)
