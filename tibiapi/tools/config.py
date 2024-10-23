from contextlib import asynccontextmanager

from fastapi import FastAPI, Request, Response
from fastapi_redis_cache import FastApiRedisCache

from tibiapi.tools.settings import Settings

settings = Settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    redis_cache = FastApiRedisCache()
    redis_cache.init(
        host_url=settings.CACHE_HOST,
        response_header="X-TibiApi-Cache",
        ignore_arg_types=[Request, Response],
    )
    yield
