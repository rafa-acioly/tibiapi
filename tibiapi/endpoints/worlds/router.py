from typing import List

from fastapi import APIRouter

from . import service
from .schemas import World, WorldDetail

router = APIRouter()


@router.get("/")
async def index() -> List[World]:
    return await service.list_worlds()


@router.get("/{world_name}")
async def find(world_name: str) -> WorldDetail:
    return await service.find_world(world_name.title())
