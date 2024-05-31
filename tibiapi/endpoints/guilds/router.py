from typing import List

from fastapi import APIRouter

from .schemas import Guild, GuildMember
from .service import find_guild, find_guild_members

router = APIRouter()


@router.get("/{guild_name}")
async def find(guild_name: str) -> Guild:
    """Find a guild by its name."""
    return await find_guild(guild_name)


@router.get("/{guild_name}/members")
async def find_members(guild_name: str, online_only: bool = False) -> List[GuildMember]:
    """Find the members of a guild by its name."""
    return await find_guild_members(guild_name, online_only)
