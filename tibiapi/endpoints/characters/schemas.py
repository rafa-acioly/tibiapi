from typing import List, Optional, Union

from pydantic import BaseModel, Field


class Badges(BaseModel):
    name: str
    icon_url: str


class Information(BaseModel):
    created: str
    loyalty_title: str


class Achievements(BaseModel):
    grade: int
    name: str
    secret: bool = False


class Guild(BaseModel):
    name: str
    rank: str


class DeathAssist(BaseModel):
    name: str
    player: str
    summon: str
    traded: bool


class DeathKiller(BaseModel):
    name: str
    player: str
    summon: str
    traded: bool


class Deaths(BaseModel):
    assists: List[DeathAssist]
    killers: List[DeathKiller]


class Character(BaseModel):
    name: str
    level: int
    sex: str
    vocation: str
    world: str
    title: str
    comment: str | None = Field(default=None)
    last_login: str
    account_status: str
    married_to: str | None = Field(default=None)
    residence: str | None
    deletion_date: str | None = Field(default=None)
    former_names: str | None = Field(default=None)
    former_world: str | None = Field(default=None)
    achievement_points: int = Field(default=0)
    traded: bool = Field(default=False)
    unlocked_titles: int = Field(default=0)
    information: Information | None = Field(default=None)
    guild_membership: str | None = Field(default=None)
