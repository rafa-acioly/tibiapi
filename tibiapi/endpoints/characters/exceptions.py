from http import HTTPStatus

from fastapi import HTTPException


class CharacterNotFound(HTTPException):
    def __init__(self, character_name: str):
        super().__init__(status_code=HTTPStatus.NOT_FOUND.value, detail=f"Character {
            character_name} not found.")
