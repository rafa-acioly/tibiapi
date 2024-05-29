import re
import unicodedata


def slugify(value: str) -> str:
    """
    Normalizes string, converts to lowercase, removes non-alpha characters,
    and converts spaces to underscores.
    """
    value = unicodedata.normalize("NFKD", value).encode(
        "ascii", "ignore").decode()
    value = re.sub(r"[^\w\s]", "", value).strip().lower()
    return re.sub(r"[_\s]+", "_", value)
