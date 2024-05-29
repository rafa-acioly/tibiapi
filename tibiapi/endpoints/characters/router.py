from typing import List

from fastapi import APIRouter
from fastapi_redis_cache import cache

from tibiapi.endpoints.characters.schemas import (
    Achievements,
    Badges,
    Character,
    Characters,
    Deaths,
)
from tibiapi.endpoints.characters.service import (
    get_achievements,
    get_character,
    get_characters,
)

router = APIRouter()


@cache(expire=10800)  # 3 hours
@router.get("/{character_name}", summary="Find a character by his name.")
async def find(character_name: str) -> Character:
    """Find a character by his name."""
    return await get_character(character_name)


@cache(expire=10800)  # 3 hours
@router.get(
    "/{character_name}/characters",
    response_model=List[Characters],
    summary="Get all characters from a specific player.")
async def find_characters(character_name: str) -> Characters:
    """Get all characters from a specific player."""
    return await get_characters(character_name)


@cache(expire=300)  # 5 minutes
@router.get(
    "/{character_name}/achievements",
    response_model=List[Achievements],
    summary="Get achievements from a character.")
async def find_achievements(character_name: str) -> Achievements:
    """Get achievements from a character."""
    return await get_achievements(character_name)


@cache(expire=10800)  # 3 hours
@router.get(
    "/{character_name}/badges",
    response_model=List[Badges],
    summary="Get badges from a character.")
async def find_badges(character_name: str) -> Badges:
    """Get badges from a character."""
    return {"character_name": character_name}


@cache(expire=120)  # 2 minutes
@router.get(
    "/{character_name}/deaths",
    response_model=Deaths,
    summary="Get deaths from a character.")
async def find_deaths(character_name: str) -> Deaths:
    """Get deaths from a character."""
    return {"character_name": character_name}
