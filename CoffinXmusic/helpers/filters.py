from typing import List, Union

from CoffinXMusic.config import COMMAND_PREFIXES
from pyrogram import filters

other_filters = filters.group & ~filters.edited & ~filters.via_bot & ~filters.forwarded
other_filters2 = (
    filters.private & ~filters.edited & ~filters.via_bot & ~filters.forwarded
)


def command(commands: Union[str, List[str]]):
    return filters.command(commands, COMMAND_PREFIXES)
