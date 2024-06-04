from fastapi import APIRouter
from fastapi_redis_cache import cache_one_hour

from . import service
from .enums import HighScoreCategory, HighScoreVocation, HighScoreWorld

router = APIRouter()


@router.get("/", summary="Get highscores from a world")
@cache_one_hour()
async def find(
    world_name: HighScoreWorld = None,
    vocation: HighScoreVocation = HighScoreVocation.NONE,
    category: HighScoreCategory = None
):
    return await service.find_highscores(world_name.title(), vocation, category)
