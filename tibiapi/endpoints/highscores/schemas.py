from pydantic import BaseModel


class HighScoreEntry(BaseModel):
    name: str
    level: int
    vocation: str
    rank: int
    title: str
    world: str


class HighScore(BaseModel):
    pass
