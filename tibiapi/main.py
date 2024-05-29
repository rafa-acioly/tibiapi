from fastapi import APIRouter, FastAPI, Request, Response
from fastapi_redis_cache import FastApiRedisCache

from tibiapi.endpoints.characters.router import router as characters
from tibiapi.endpoints.guilds.router import router as guilds
from tibiapi.endpoints.worlds.router import router as worlds
from tibiapi.routes import api_routes
from tibiapi.tools.settings import Settings

settings = Settings()

app = FastAPI(title="TibiAPI", version="0.0.1")
app.include_router(api_routes)


@app.on_event("startup")
def startup():
    redis_cache = FastApiRedisCache()
    redis_cache.init(
        host_url=settings.CACHE_HOST,
        response_header="X-TibiApi-Cache",
        ignore_arg_types=[Request, Response]
    )
