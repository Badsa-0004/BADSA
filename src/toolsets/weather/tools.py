"""
Weather tool for BADSA.

Provides current weather information using the Open-Meteo service.
"""

from typing import Annotated
import logging

from livekit.agents import RunContext, function_tool

from config import settings
from .service import (
    get_weather_by_city,
    weather_description,
)

logger = logging.getLogger(__name__)


@function_tool()
async def get_weather(
    context: RunContext,
    city: str | None = None,
) -> str:
    """
    Get the current weather for a city.

    Use this tool whenever the user asks about:

    - current weather
    - today's weather
    - temperature
    - humidity
    - wind
    - rain
    - climate
    - how hot or cold it is

    Args:
        city:
            Optional city name.
            If omitted, the configured default city is used.
    """

    city = city or settings.default_city

    logger.info("Executing tool: get_weather(city=%s)", city)

    try:
        weather, location = await get_weather_by_city(city)

        current = weather["current"]

        description = weather_description(
            current["weather_code"]
        ).lower()

        temperature = current["temperature_2m"]
        feels_like = current["apparent_temperature"]
        humidity = current["relative_humidity_2m"]
        wind_speed = current["wind_speed_10m"]

        return (
            f"It's currently {temperature}°C and {description} in {location}. "
            f"It feels like {feels_like}°C. "
            f"The humidity is {humidity}% and "
            f"the wind speed is {wind_speed} km/h."
        )

    except ValueError as exc:
        logger.warning("Unknown city '%s': %s", city, exc)

        return (
            f"I couldn't find the location '{city}'. "
            "Please check the city name and try again."
        )

    except Exception:
        logger.exception("Weather tool failed")

        return (
            f"Sorry, I couldn't retrieve the weather for {city} at the moment. "
            "Please try again later."
        )