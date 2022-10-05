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
    sex: str
    vocation: str
    world: str
    title: str
    comment: str
    deletion_date: Optional[str]
    account_status: str
    former_names: List[str] = Field(default=[])
    former_worlds: List[str] = Field(default=[])
    achievement_points: int = Field(default=0)
    last_login: str
    level: int
    married_to: Optional[str]
    residence: Optional[str]
    traded: bool = Field(default=False)
    unlocked_titles: Optional[int]
    badges: List[Badges] = Field(default=[])
    information: Optional[Information]
    guild: Optional[Guild]
    achievements: List[Achievements] = Field(default=[])
    deaths: List[Deaths] = Field(default=[])
