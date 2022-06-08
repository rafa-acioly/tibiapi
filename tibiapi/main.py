from fastapi import APIRouter, FastAPI

from tibiapi.endpoints.characters.router import router as characters
from tibiapi.endpoints.guilds.router import router as guilds
from tibiapi.endpoints.worlds.router import router as worlds

api_router = APIRouter()
api_router.include_router(characters, prefix="/characters")
api_router.include_router(guilds, prefix="/guilds")
api_router.include_router(worlds, prefix="/worlds")


app = FastAPI(title="TibiAPI", version="0.0.1")
app.include_router(api_router)