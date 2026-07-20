"""
Date and Time tools for BADSA.
"""

from datetime import datetime

from livekit.agents import RunContext, function_tool


class DateTimeTools:
    """Date and Time related tools."""

    @function_tool
    async def get_current_datetime(self, context: RunContext) -> str:
        """
        Get the current local date and time.

        Use this tool whenever the user asks:
        - What time is it?
        - What's today's date?
        - What day is today?
        - Current date and time
        """

        now = datetime.now()

        return (
            f"Current date and time: "
            f"{now.strftime('%A, %d %B %Y, %I:%M:%S %p')}"
        )