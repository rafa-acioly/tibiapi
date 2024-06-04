from fastapi import APIRouter
from fastapi_redis_cache import cache_one_hour

from . import service
from .enums import HighScoreCategory, HighScoreVocation, HighScoreWorld
from .schemas import HighScore, HighScoreEntry

router = APIRouter()


@router.get("", summary="Get highscores")
async def index(
    world_name: HighScoreWorld = None,
    vocation: HighScoreVocation = None,
    category: HighScoreCategory = None
) -> list[HighScoreEntry]:
    return await service.find_highscores(world_name, vocation, category)
