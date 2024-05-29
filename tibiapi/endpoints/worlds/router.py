from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def index():
    return {"worlds": "worlds"}


@router.get("/{world_name}")
async def find(world_name: str):
    return {"world_name": world_name}
