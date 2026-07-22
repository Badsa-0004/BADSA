from datetime import datetime
import logging

from livekit.agents import RunContext, function_tool

logger = logging.getLogger(__name__)


@function_tool()
async def get_current_datetime(context: RunContext) -> str:
    """
    Purpose:
        Retrieve the current local date and time.

    Use this tool when the user asks about:
        - current time
        - current date
        - today's date
        - today's time
        - today's day
        - weekday
        - day of the week
        - month
        - year
        - local date
        - local time
        - what time it is
        - what day it is

    This tool is the authoritative source for all date and time
    information.

    Never answer date or time questions using internal knowledge if
    this tool can be used.

    Returns:
        A human-readable string containing the current local date and
        time.
    """

    logger.info("get_current_datetime tool executed")

    now = datetime.now()

    return now.strftime(
        "Current date and time: %A, %d %B %Y, %I:%M:%S %p"
    )