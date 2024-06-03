from typing import List

from pydantic import BaseModel, Field


class World(BaseModel):
    name: str
    players_online: int
    pvp_type: str
    location: str
    additional_information: str | None = Field(default=None)


class WorldQuestTitle(BaseModel):
    name: str
    href: str


class WorldOnlineRecord(BaseModel):
    players: int
    date: str


class WorldDetail(BaseModel):
    status: str
    players_online: int
    online_record: WorldOnlineRecord
    creation_date: str
    location: str
    pvp_type: str
    world_quest_titles: List[str]
    battleye_status: str
    game_world_type: str
