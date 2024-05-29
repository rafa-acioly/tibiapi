from fastapi import APIRouter

from tibiapi.endpoints.characters.router import router as characters
from tibiapi.endpoints.guilds.router import router as guilds
from tibiapi.endpoints.worlds.router import router as worlds

api_routes = APIRouter(prefix="/api/v1")

"""
|--------------------------------------------------------------------------
| API Routes
|--------------------------------------------------------------------------
|
| Here is where we can register API routes for the application.
"""
api_routes.include_router(characters, prefix="/character", tags=['Character'])
api_routes.include_router(guilds, prefix="/guilds", tags=['Guilds'])
api_routes.include_router(worlds, prefix="/worlds", tags=['Worlds'])
