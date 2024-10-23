from bs4.element import ResultSet, Tag

from tibiapi.tools import stringify_number

from .enums import HighScoreCategory
from .schemas import HighScoreEntry


def extract_players_highscore(
    category: HighScoreCategory, content: ResultSet[Tag]
) -> list[HighScoreEntry]:
    """
    Parse the high score information from the content.
    """

    # The loyalty points highscore has an extra column for the title.
    # The default highscore has 6 columns, while the loyalty points highscore has 7.
    if category is HighScoreCategory.LOYALTY_POINTS:
        return _extract_loyalty_points(content)

    return _extract_default_table(content)


def _extract_default_table(content: ResultSet[Tag]) -> list[HighScoreEntry]:
    """
    Extract default values from table.
    """
    players: HighScoreEntry = []

    # Skip the first two rows, which are menu and headers.
    for row in content[2:]:
        data = row.find_all("td")

        exp_points = data[5].text.replace(",", "")

        players.append(
            HighScoreEntry(
                rank=int(data[0].text),
                name=data[1].find("a").text,
                vocation=data[2].text,
                world=data[3].text,
                level=int(data[4].text),
                points=stringify_number(exp_points),
            )
        )

    return players


def _extract_loyalty_points(content: ResultSet[Tag]) -> list[HighScoreEntry]:
    """
    Extract Loyalty points highscore.
    """

    players: HighScoreEntry = []

    # Skip the first two rows, which are menu and headers.
    for row in content[2:]:
        data = row.find_all("td")

        exp_points = data[6].text.replace(",", "")

        players.append(
            HighScoreEntry(
                rank=int(data[0].text),
                name=data[1].find("a").text,
                title=data[2].text,
                vocation=data[3].text,
                world=data[4].text,
                level=int(data[5].text),
                points=stringify_number(exp_points),
            )
        )

    return players
