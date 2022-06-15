from fastapi import APIRouter

from tibiapi.endpoints.characters.schemas import (
    Achievements,
    Badges,
    Character,
    Deaths,
    Guild,
    Information,
)
from tibiapi.endpoints.characters.service import get_character

router = APIRouter()


@router.get("/{character_name}")
async def find(character_name: str) -> Character:
    """Find a character by his name."""
    result = await get_character(character_name)

    return result


@router.get("/{character_name}/achievements", response_model=Achievements)
async def find_achievements(character_name: str) -> Achievements:
    """Get achievements from a character."""
    return {"character_name": character_name}


@router.get("/{character_name}/badges", response_model=Badges)
async def find_badges(character_name: str) -> Badges:
    """Get badges from a character."""
    return {"character_name": character_name}


@router.get("/{character_name}/deaths", response_model=Deaths)
async def find_deaths(character_name: str) -> Deaths:
    """Get deaths from a character."""
    return {"character_name": character_name}


@router.get("/{character_name}/guild", response_model=Guild)
async def find_guild(character_name: str) -> Guild:
    """Get guild from a character."""
    return {"character_name": character_name}


@router.get("/{character_name}/information", response_model=Information)
async def find_information(character_name: str) -> Information:
    """Get information from a character."""
    return {"character_name": character_name}
