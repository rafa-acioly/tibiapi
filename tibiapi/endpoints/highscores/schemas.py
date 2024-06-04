from pydantic import BaseModel


class HighScoreEntry(BaseModel):
    rank: int
    name: str
    vocation: str
    world: str
    level: int
    points: str


class HighScore(BaseModel):
    scores: list[HighScoreEntry]
