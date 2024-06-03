from typing import List

from fastapi import APIRouter

from .schemas import World
from .service import list_worlds

router = APIRouter()


@router.get("/")
async def index() -> List[World]:
    return await list_worlds()


@router.get("/{world_name}")
async def find(world_name: str):
    return {"world_name": world_name}
