import re as regex

from bs4.element import ResultSet

from tibiapi.tools.sieve import extract_table_information

from .schemas import WorldDetail, WorldOnlineRecord


def extract_world_detail(content: ResultSet) -> WorldDetail:
    """Extract the world detail from the content."""

    data = extract_table_information(content)

    online_record_pattern = r"([\d,]+) players \(on (.*?)\)"
    match = regex.match(online_record_pattern, data["online_record"])

    record = WorldOnlineRecord(
        players=int(match.group(1).replace(",", "").strip()), date=match.group(2)
    )

    formatted_data = data | {
        "online_record": record,
        "world_quest_titles": data["world_quest_titles"].split(", "),
    }

    return WorldDetail(**formatted_data)
