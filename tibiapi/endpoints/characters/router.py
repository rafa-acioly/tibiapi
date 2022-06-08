from fastapi import APIRouter

from tibiapi.endpoints.characters.schemas import Character

router = APIRouter()


@router.get("/{character_name}/", response_model=Character)
async def find(character_name: str) -> Character:
    """Find a character by his name."""
    return {"character_name": character_name}