import sentry_sdk
from fastapi import FastAPI, Request, Response
from fastapi_redis_cache import FastApiRedisCache
from sentry_sdk.integrations.fastapi import FastApiIntegration
from sentry_sdk.integrations.starlette import StarletteIntegration

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

    sentry_sdk.init(
        dsn=settings.SENTRY_DSN,
        traces_sample_rate=1.0,
        profiles_sample_rate=1.0,
        integrations=[
            StarletteIntegration(transaction_style="endpoint"),
            FastApiIntegration(transaction_style="endpoint")
        ]
    )
