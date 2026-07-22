from datetime import datetime
import logging

from livekit.agents import RunContext, function_tool

logger = logging.getLogger(__name__)


@function_tool()
async def get_current_datetime(context: RunContext) -> str:
    """
    Get the current date and local time.

    Use this tool whenever the user asks about:

    - current time
    - current date
    - today's date
    - today's day
    - weekday
    - day of the week
    - month
    - year
    - local date
    - local time

    Always use this tool instead of relying on internal knowledge,
    because the current date and time constantly change.

    Returns:
        The current date and local time formatted for natural speech.
    """

    logger.info("Executing tool: get_current_datetime")

    now = datetime.now()

    formatted_datetime = now.strftime(
        "%A, %d %B %Y at %I:%M:%S %p"
    )

    return f"Current date and local time: {formatted_datetime}"