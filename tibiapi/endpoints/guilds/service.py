import re as regex
from typing import Dict, List

import tibiapi.tools.strainer as strainer
from tibiapi.gateway import client
from tibiapi.tools import slugify

from .enums import GuildPageIdentifiers
from .schemas import Guild, GuildHall, GuildMember, GuildMemberInvite


async def find_guild(guild_name: str) -> Guild:
    """
    Get a guild by its name.
    The guild information is scraped from the Tibia.com website.

    The HTML element that contains the guild information contains
    the following structure:

    <div id="GuildInformationContainer">
        We took over this ship. <br><br>
        The guild was founded on {{ server }} on {{ date }}.<br>
        It is currently {{ status }}.<br>
        Guild is opened for applications.<br>
        The official homepage is at {{ link }}.<br>
        Their home on {{ server }} is {{ guild_hall }}. The rent is paid until {{ date }}<br>
    </div>

    The guild information is split by new lines and the information is
    extracted from the text.
    """
    page = await client.get_guild(guild_name)

    guild_info_container = page.select_one(
        GuildPageIdentifiers.INFORMATION_CONTAINER.value)
    guild_paragraphs = guild_info_container.text.split("\n")

    foundation = _parse_guild_foundation(guild_paragraphs)

    return Guild(
        name=guild_name,
        world=foundation["world"],
        active=_parse_guild_status(guild_paragraphs),
        open_applications=_parse_guild_application(guild_paragraphs),
        guild_hall=_parse_guild_hall(guild_paragraphs),
        foundation_date=foundation["foundation_date"],
        homepage=_parse_guild_homepage(guild_paragraphs),
    )


async def find_guild_members(guild_name: str, online: bool | None = False) -> List[GuildMember]:
    """
    Get the members of a guild by its name.

    **The table that contains the guild members is a real mess**, the first "row"
    contains the table title, it's not a real row, so we need to skip it.
    The second row contains the table headers along with the
    information of the first member, for now,
    we are going to skip it.
    """
    # TODO: Find a way to get the first and second member information without skipping the rows

    page = await client.get_guild(guild_name)

    members_table = page.select_one(".TableContainer table.Table3")
    table_rows = members_table.select("tr[bgcolor]") if not online else members_table.select(
        "tr[bgcolor]:has(td:-soup-contains('online'))")

    members: List[GuildMember] = []
    for row in table_rows[2:]:
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


async def find_guild_members_invite(guild_name: str) -> List[GuildMemberInvite]:
    """Get the invited members of a guild by its name."""

    page = await client.get_guild(guild_name)

    invitation_container = page.select(".TableContentContainer")
    invitation_table = invitation_container[len(invitation_container) - 4]

    # The first row is the table header and it has class "LabelH", we need to skip it
    invitations = invitation_table.select("tr:not(.LabelH)")

    invited_members: List[GuildMemberInvite] = []
    for invitation in invitations:
        cells = invitation.find_all("td")

        invited_members.append(GuildMemberInvite(
            name=cells[0].find("a").text,
            invitation_date=cells[1].text,
        ))

    return invited_members


def _parse_guild_foundation(paragraphs: List[str]) -> Dict[str, str]:
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


def _parse_guild_hall(paragraphs: List[str]) -> GuildHall:
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


def _parse_guild_status(paragraphs: List[str]) -> bool:
    """
    Parse the guild status from the guild information.

    The guild status is in the following format:
    "It is currently {{ status }}."
    """

    for paragraph in paragraphs:
        if paragraph.startswith("It is currently"):
            return "active" in paragraph

    return False


def _parse_guild_application(paragraphs: List[str]) -> bool:
    """
    Parse the guild application status from the guild information.

    The guild application status is in the following format:
    "Guild is opened for applications."
    """

    for paragraph in paragraphs:
        if paragraph.startswith("Guild is") and "opened" in paragraph:
            return True

    return False


def _parse_guild_homepage(paragraphs: List[str]) -> str:
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
