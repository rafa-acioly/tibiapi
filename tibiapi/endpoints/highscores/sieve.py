from bs4.element import ResultSet, Tag

from tibiapi.tools import stringify_number

from .schemas import HighScoreEntry


def extract_players_highscore(content: ResultSet[Tag]) -> list[HighScoreEntry]:
    """
    Parse the high score information from the content.
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
                points=stringify_number(exp_points)
            )
        )

    return players
