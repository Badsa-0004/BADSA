"""
Weather service for BADSA.

Handles communication with the Open-Meteo APIs.

Responsibilities:
- Convert city names into coordinates.
- Retrieve current weather.
- Translate weather codes into human-readable descriptions.
"""

import httpx

GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
WEATHER_URL = "https://api.open-meteo.com/v1/forecast"

WEATHER_CODES = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Depositing rime fog",
    51: "Light drizzle",
    53: "Moderate drizzle",
    55: "Dense drizzle",
    61: "Light rain",
    63: "Moderate rain",
    65: "Heavy rain",
    71: "Light snow",
    73: "Moderate snow",
    75: "Heavy snow",
    80: "Rain showers",
    81: "Heavy rain showers",
    82: "Violent rain showers",
    95: "Thunderstorm",
}


def weather_description(code: int) -> str:
    """
    Convert an Open-Meteo weather code into
    a human-readable description.
    """
    return WEATHER_CODES.get(code, "Unknown weather")


async def get_coordinates(city: str) -> tuple[float, float, str]:
    """
    Convert a city name into latitude and longitude.

    Returns:
        latitude,
        longitude,
        resolved location name
    """

    async with httpx.AsyncClient(timeout=10) as client:

        response = await client.get(
            GEOCODING_URL,
            params={
                "name": city,
                "count": 1,
                "language": "en",
                "format": "json",
            },
        )

        response.raise_for_status()

        data = response.json()

    results = data.get("results")

    if not results:
        raise ValueError(f"Could not find location '{city}'.")

    location = results[0]

    location_name = location["name"]

    country = location.get("country")

    if country:
        location_name = f"{location_name}, {country}"

    return (
        location["latitude"],
        location["longitude"],
        location_name,
    )


async def get_current_weather(
    latitude: float,
    longitude: float,
) -> dict:
    """
    Retrieve current weather from Open-Meteo.
    """

    async with httpx.AsyncClient(timeout=10) as client:

        response = await client.get(
            WEATHER_URL,
            params={
                "latitude": latitude,
                "longitude": longitude,
                "current": [
                    "temperature_2m",
                    "relative_humidity_2m",
                    "apparent_temperature",
                    "wind_speed_10m",
                    "weather_code",
                ],
            },
        )

        response.raise_for_status()

        return response.json()


async def get_weather_by_city(
    city: str,
) -> tuple[dict, str]:
    """
    Retrieve the current weather for a city.

    Args:
        city:
            City name.

    Returns:
        Tuple containing:
            - weather data
            - resolved location name
    """

    latitude, longitude, location = await get_coordinates(city)

    weather = await get_current_weather(
        latitude,
        longitude,
    )

    return weather, location