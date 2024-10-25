from fastapi import APIRouter
from fastapi_redis_cache import cache_one_day

router = APIRouter()


@router.get("/{event_name}", summary="Find an event by its name.")
@cache_one_day()
async def find(event_name: str):
    return {"event_name": event_name}
