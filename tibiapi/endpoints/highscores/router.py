from fastapi import APIRouter
from fastapi_redis_cache import cache_one_month

from tibiapi.endpoints.worlds.enums import World

from . import service
from .enums import HighScoreCategory, HighScoreVocation
from .schemas import HighScoreEntry

router = APIRouter()


@router.get("", summary="Get highscores")
@cache_one_month()
async def index(
    world_name: World = None,
    vocation: HighScoreVocation = None,
    category: HighScoreCategory = None
) -> list[HighScoreEntry]:
    return await service.find_highscores(world_name, vocation, category)
