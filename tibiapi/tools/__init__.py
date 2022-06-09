import re
import unicodedata


# slugify a string using underscore
def slugify(value: str) -> str:
    """
    Normalizes string, converts to lowercase, removes non-alpha characters,
    and converts spaces to underscores.
    """
    value = str(value)
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub("[^\w\s-]", '', value).strip().lower()
    value = re.sub('[\s]+', '_', value)
    return value
