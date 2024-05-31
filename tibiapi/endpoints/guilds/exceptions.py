from http import HTTPStatus

from fastapi import HTTPException


class GuildNotFound(HTTPException):

    def __init__(self, guild_name: str):
        super().__init__(status_code=HTTPStatus.NOT_FOUND.value,
                         detail=f"guild {guild_name} not found")
