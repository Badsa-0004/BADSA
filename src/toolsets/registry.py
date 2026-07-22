from livekit.agents.llm import Toolset

from .datetime import get_current_datetime
from .weather import get_weather

CORE_TOOLSET = Toolset(
    id="core",
    tools=[
        get_current_datetime,
        get_weather,
    ],
)