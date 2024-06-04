from typing import List

from fastapi import APIRouter
from fastapi_redis_cache import cache_one_hour, cache_one_month

from . import service
from .schemas import World, WorldDetail

router = APIRouter()


@router.get("/")
@cache_one_month()
async def index() -> List[World]:
    return await service.list_worlds()


@router.get("/{world_name}")
@cache_one_hour()
async def find(world_name: str) -> WorldDetail:
    return await service.find_world(world_name.title())
