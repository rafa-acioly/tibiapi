from typing import Any, Dict, Generic, TypeVar

T = TypeVar('T')


class Pick(Generic[T]):
    def __init__(self, original: T, *fields: str):
        self._picked: Dict[str, Any] = {
            field: getattr(original, field) for field in fields}

    def __getattr__(self, item: str) -> Any:
        if item in self._picked:
            return self._picked[item]
        raise AttributeError(
            f"'{self.__class__.__name__}' object has no attribute '{item}'")
