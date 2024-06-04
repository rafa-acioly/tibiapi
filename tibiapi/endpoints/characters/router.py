from typing import List

from fastapi import APIRouter
from fastapi_redis_cache import cache, cache_one_day

from tibiapi.endpoints.characters.schemas import (
    Achievements,
    Character,
    Characters,
    Deaths,
)

from . import service

router = APIRouter()


@router.get("/{character_name}", summary="Find a character by his name.")
@cache_one_day()
async def find(character_name: str) -> Character:
    """Find a character by his name."""
    return await service.get_character(character_name)


@router.get(
    "/{character_name}/characters",
    response_model=List[Characters],
    summary="Get all characters from a specific player.")
@cache_one_day()
async def find_characters(character_name: str) -> Characters:
    """Get all characters from a specific player."""
    return await service.get_characters(character_name)


@router.get(
    "/{character_name}/achievements",
    response_model=List[Achievements],
    summary="Get achievements from a character.")
@cache(expire=300)  # 5 minutes
async def find_achievements(character_name: str) -> Achievements:
    """Get achievements from a character."""
    return await service.get_achievements(character_name)


@router.get(
    "/{character_name}/deaths",
    response_model=Deaths,
    summary="Get deaths from a character.")
@cache(expire=120)  # 2 minutes
async def find_deaths(character_name: str) -> Deaths:
    """Get deaths from a character."""
    return {"character_name": character_name}
