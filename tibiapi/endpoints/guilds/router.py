from typing import List

from fastapi import APIRouter

from . import service
from .schemas import Guild, GuildMember, GuildMemberInvite

router = APIRouter()


@router.get("/{guild_name}", summary="Find a guild by its name.")
async def find(guild_name: str) -> Guild:
    """Find a guild by its name."""
    return await service.find_guild(guild_name)


@router.get("/{guild_name}/members", summary="Find all the members of a guild by its name.")
async def find_members(guild_name: str, online: bool = False) -> List[GuildMember]:
    """Find the members of a guild by its name."""
    return await service.find_guild_members(guild_name, online)


@router.get(
    "/{guild_name}/members/invites",
    summary="Find all the invited members of a guild by its name.")
async def find_invites(guild_name: str) -> List[GuildMemberInvite]:
    """Find the invited members of a guild by its name."""
    return await service.find_guild_members_invite(guild_name)
