from pydantic import BaseModel, Field


class HighScoreEntry(BaseModel):
    rank: int
    name: str
    vocation: str
    world: str
    level: int
    points: str
    title: str | None = Field(default=None)


class HighScore(BaseModel):
    scores: list[HighScoreEntry]
