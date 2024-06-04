from fastapi import APIRouter
from fastapi_redis_cache import cache_one_hour

from . import service
from .enums import HighScoreCategory, HighScoreVocation, HighScoreWorld
from .schemas import HighScore

router = APIRouter()


@router.get("/", summary="Get highscores from a world")
@cache_one_hour()
async def find(
    world_name: HighScoreWorld = None,
    vocation: HighScoreVocation = HighScoreVocation.NONE,
    category: HighScoreCategory = None
) -> HighScore:
    return await service.find_highscores(world_name.title(), vocation, category)
