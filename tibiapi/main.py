from fastapi import APIRouter, FastAPI

from tibiapi.endpoints.characters.router import router as characters
from tibiapi.endpoints.guilds.router import router as guilds
from tibiapi.endpoints.worlds.router import router as worlds

app = FastAPI(title="TibiAPI", version="0.0.1")
api_router = APIRouter(prefix="/api/v1")

"""
|--------------------------------------------------------------------------
| API Routes
|--------------------------------------------------------------------------
|
| Here is where we can register API routes for the application.
"""
api_router.include_router(characters, prefix="/characters", tags=['Character'])
api_router.include_router(guilds, prefix="/guilds", tags=['Guilds'])
api_router.include_router(worlds, prefix="/worlds", tags=['Worlds'])

app.include_router(api_router)
