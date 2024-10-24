from typing import List

import tibiapi.endpoints.guilds.sieve as sieve

from .client import get_guild
from .enums import GuildPageIdentifiers
from .schemas import Guild, GuildMember, GuildMemberInvite


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

    page = await get_guild(guild_name)

    guild_info_container = page.select_one(
        GuildPageIdentifiers.INFORMATION_CONTAINER.value
    )
    guild_paragraphs = guild_info_container.text.split("\n")

    foundation = sieve.extract_guild_foundation(guild_paragraphs)

    return Guild(
        name=guild_name,
        world=foundation["world"],
        active=sieve.extract_guild_status(guild_paragraphs),
        open_applications=sieve.extract_guild_application(guild_paragraphs),
        guild_hall=sieve.extract_guild_hall(guild_paragraphs),
        foundation_date=foundation["foundation_date"],
        homepage=sieve.extract_guild_homepage(guild_paragraphs),
    )


async def find_guild_members(
    guild_name: str, online: bool | None = False
) -> List[GuildMember]:
    """Get the members of a guild by its name."""

    page = await get_guild(guild_name)

    members_table = page.select_one(".TableContainer table.Table3")

    # The table rows are colored, so we can filter them by the bgcolor attribute.
    # Players that are online have a green status, so we can filter them by that.
    table_rows = (
        members_table.select("tr[bgcolor]")
        if not online
        else members_table.select("tr[bgcolor]:has(td.onlinestatus > span.green)")
    )

    return sieve.extract_guild_members(table_rows)


async def find_guild_members_invite(guild_name: str) -> List[GuildMemberInvite]:
    """Get the invited members of a guild by its name."""

    page = await get_guild(guild_name)

    invitation_container = page.select_one(
        ".TableContentContainer:has(table.TableContent:has(tr.Odd))"
    )

    if not invitation_container:
        return []

    return sieve.extract_guild_member_invite(invitation_container)
