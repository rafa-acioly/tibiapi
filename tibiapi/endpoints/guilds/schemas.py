from pydantic import BaseModel, Field


class GuildHall(BaseModel):
    name: str | None = Field(default=None)
    paid_until: str | None = Field(default=None)


class Guild(BaseModel):
    name: str
    world: str
    active: bool
    open_applications: bool
    guild_hall: GuildHall
    foundation_date: str
    homepage: str | None = Field(default=None)
