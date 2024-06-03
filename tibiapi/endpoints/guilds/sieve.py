import re as regex
from typing import Dict, List

from bs4.element import ResultSet, Tag

from .schemas import GuildHall, GuildMember


def extract_guild_foundation(paragraphs: List[str]) -> Dict[str, str]:
    """
    Parse the foundation date from the guild information.

    The foundation date is in the following format:
    "The guild was founded on {{ server }} on {{ date }}."
    """

    for paragraph in paragraphs:
        if paragraph.startswith("The guild was founded"):
            pattern = r"on (\w+) on (.+)\."
            match = regex.search(pattern, paragraph)

            return {"world": match.group(1), "foundation_date": match.group(2)}


def extract_guild_hall(paragraphs: List[str]) -> GuildHall:
    """
    Parse the guild hall information from the guild information.
    The guild hall information contains the world, the name of the guild hall,
    and the date until the rent is paid.

    The guild hall information is in the following format:
    "Their home on {{ server }} is {{ guild_hall }}. The rent is paid until {{ date }}"
    """

    for paragraph in paragraphs:
        if paragraph.startswith("Their home"):
            pattern = r"is ([^.]+)\. .* until (.+)\.$"
            match = regex.search(pattern, paragraph)

            return GuildHall(name=match.group(1), paid_until=match.group(2))

    return GuildHall()


def extract_guild_status(paragraphs: List[str]) -> bool:
    """
    Parse the guild status from the guild information.

    The guild status is in the following format:
    "It is currently {{ status }}."
    """

    for paragraph in paragraphs:
        if paragraph.startswith("It is currently"):
            return "active" in paragraph

    return False


def extract_guild_application(paragraphs: List[str]) -> bool:
    """
    Parse the guild application status from the guild information.

    The guild application status is in the following format:
    "Guild is opened for applications."
    """

    for paragraph in paragraphs:
        if paragraph.startswith("Guild is") and "opened" in paragraph:
            return True

    return False


def extract_guild_homepage(paragraphs: List[str]) -> str:
    """
    Parse the guild homepage from the guild information.

    The guild homepage is in the following format:
    "The official homepage is at {{ link }}."
    """

    for paragraph in paragraphs:
        if paragraph.startswith("The official homepage"):
            pattern = r"at (.+)\.$"
            match = regex.search(pattern, paragraph)

            return match.group(1)

    return None


def extract_guild_members(tags: ResultSet[Tag]) -> List[GuildMember]:
    """
    Extract the guild members from the guild page table. The second row contains
    the table headers along with the information of the first member,
    for now, we are going to skip it.
    """

    members: List[GuildMember] = []

    # TODO: Find a way to get the first and second member information without skipping the rows
    for row in tags[2:]:
        cells = row.find_all("td")
        cell_content = cells[1].text

        # The member name is inside an <a> tag
        # The title is the text after the member name
        member_name = cells[1].find("a").text
        title = cell_content.replace(
            member_name, "").replace("(", "").replace(")", "")

        members.append(GuildMember(
            rank=cells[0].text if len(cells[0].text.strip()) > 0 else None,
            name=cells[1].find("a").text,
            title=title.strip() if len(title.strip()) > 0 else None,
            vocation=cells[2].text,
            level=cells[3].text,
            joining_date=cells[4].text,
            status=cells[5].text,
        ))

    return members


def extract_guild_member_invite(tag: Tag) -> List[GuildMember]:
    """Extract the invited guild members from the guild page table."""

    # The first row is the table header and it has class "LabelH", we need to skip it
    invitations = tag.select("tr:not(.LabelH)")

    invited_members: List[GuildMember] = []
    for invitation in invitations[1:]:
        cells = invitation.find_all("td")

        invited_members.append(GuildMember(
            name=cells[0].find("a").text,
            rank=cells[1].text if len(cells[1].text.strip()) > 0 else None,
            vocation=cells[2].text,
            level=cells[3].text,
            invited_by=cells[4].text,
            date=cells[5].text,
        ))

    return invited_members
