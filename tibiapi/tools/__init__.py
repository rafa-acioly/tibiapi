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


def stringify_number(value: str) -> str:
    """
    Convert a string into a friendly number representation.
    The thousand values are represented with "K",
    the million values are represented with "M",
    and the billion values are represented with "B".
    """

    number = int(value.replace(",", ""))

    if abs(number) >= 1_000_000_000:
        return f"{number / 1_000_000_000:.1f}B"
    elif abs(number) >= 1_000_000:
        return f"{number / 1_000_000:.1f}M"
    elif abs(number) >= 1_000:
        return f"{number / 1_000:.1f}K"
    else:
        return str(number)
