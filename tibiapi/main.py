from fastapi import FastAPI

from tibiapi.routes import api_routes
from tibiapi.tools.config import lifespan

app = FastAPI(title="TibiAPI", version="0.0.1", lifespan=lifespan)
app.include_router(api_routes)
