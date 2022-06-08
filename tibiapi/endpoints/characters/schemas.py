from typing import List

from pydantic import BaseModel


class Badges(BaseModel):
    name: str
    icon_url: str
    description: str


class Information(BaseModel):
    created: str
    position: str
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
    deletion_date: str
    account_status: str
    former_names: List[str]
    former_worlds: List[str]
    achievement_points: int
    last_login: str
    level: int
    married_to: str
    residence: str
    traded: bool
    unlocked_titles: int
    badges: List[Badges]
    information: Information
    guild: Guild
    achievements: List[Achievements]
    deaths: List[Deaths]