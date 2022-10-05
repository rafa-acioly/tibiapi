from typing import List, Optional, Union

from pydantic import BaseModel, Field


class Badges(BaseModel):
    name: str
    icon_url: str
    description: str


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
    comment: str
    last_login: str
    account_status: str
    married_to: str | None
    residence: str | None
    deletion_date: str | None
    former_names: List[str] = Field(default=[])
    former_worlds: List[str] = Field(default=[])
    achievement_points: int = Field(default=0)
    traded: bool = Field(default=False)
    unlocked_titles: int = Field(default=0)
    badges: List[Badges] = Field(default=[])
    information: Information | None
    guild: Guild | None
    achievements: List[Achievements] = Field(default=[])
    deaths: List[Deaths] = Field(default=[])
