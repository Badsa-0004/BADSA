from livekit.agents.llm import Toolset

from .datetime import get_current_datetime


CORE_TOOLSET = Toolset(
    id="core",
    tools=[
        get_current_datetime,
    ],
)