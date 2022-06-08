from fastapi import APIRouter

router = APIRouter()


@router.get("/{guild_name}/")
async def find(guild_name: str):
    return {"guild_name": guild_name}
