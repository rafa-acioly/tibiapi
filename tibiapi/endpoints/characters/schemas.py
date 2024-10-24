from typing import List

from pydantic import BaseModel, Field


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


class Deaths(BaseModel):
    date: str
    death_level: int
    killers: List[str] = []


class Characters(BaseModel):
    name: str
    world: str
    main: bool = Field(default=False)
    status: str | None = Field(default=None)


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
    guild_membership: str | None = Field(default=None)

    # TODO: Buscar informação em outra div
    # account_information: Information | None = Field(default=None)

    def to_dict(self):
        return self.model_dump_json()

    @classmethod
    def from_dict(cls, data):
        return cls(**data)
