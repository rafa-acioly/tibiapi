import re
import unicodedata
from collections import defaultdict


def extract_table_information(content: list) -> dict:
    """
    Build a dictionary from the table content. This is mainly used when
    the table has only two columns representing a key and a value
    without any special formatting.

    Example:
        |      Account information      |
        |---------------------|---------|
        | Loyalty Title       | text    |
        | Title               | text    |

    The example above will generate a dict with the following fields:

    Example:
        {
            "loyalty_title": "text",
            "created": "text"
        }
    """

    rows = zip(*(iter(content.find_all("td")),) * 2)
    mapped_content = defaultdict(str)
    for row in rows:
        column_name, column_value = row
        mapped_content[slugify(column_name.text)] = column_value.text

    return mapped_content


def slugify(value: str) -> str:
    """
    Normalizes string, converts to lowercase, removes non-alpha characters,
    and converts spaces to underscores.
    """
    value = unicodedata.normalize('NFKD', value).encode(
        'ascii', 'ignore').decode('ascii')
    value = re.sub("[^\w\s-]", '', value).strip().lower()
    value = re.sub('[\s]+', '_', value)
    return value
