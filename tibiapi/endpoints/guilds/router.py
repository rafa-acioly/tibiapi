from fastapi import APIRouter

from .service import find_guild

router = APIRouter()


@router.get("/{guild_name}")
async def find(guild_name: str):
    """Find a guild by its name."""
    return await find_guild(guild_name)
