from fastapi import APIRouter
from fastapi_redis_cache import cache

router = APIRouter()


@router.get("/healthcheck")
async def index():
    return {"status": "ok"}
