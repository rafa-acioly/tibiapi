from pydantic import BaseModel, Field


class World(BaseModel):
    name: str
    players_online: int
    pvp_type: str
    location: str
    additional_information: str | None = Field(default=None)
