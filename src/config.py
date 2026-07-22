"""
BADSA Configuration

Loads all application settings from .env.local using pydantic-settings.
This file should be the ONLY place that reads environment variables.
"""

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings."""

    model_config = SettingsConfigDict(
        env_file=".env.local",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # -------------------------
    # Application
    # -------------------------
    app_name: str = Field(default="BADSA", alias="APP_NAME")
    app_env: str = Field(default="development", alias="APP_ENV")
    log_level: str = Field(default="INFO", alias="LOG_LEVEL")
    
    # -------------------------
    # Assistant
    # -------------------------
    voice: str = Field(default="charon", alias="BADSA_VOICE")

    # -------------------------
    # LiveKit
    # -------------------------
    livekit_url: str = Field(alias="LIVEKIT_URL")
    livekit_api_key: str = Field(alias="LIVEKIT_API_KEY")
    livekit_api_secret: str = Field(alias="LIVEKIT_API_SECRET")

    # -------------------------
    # Gemini
    # -------------------------
    google_api_key: str = Field(alias="GOOGLE_API_KEY")

    # -------------------------
    # Memory
    # -------------------------
    memory_path: str = Field(default="memory/memory.json", alias="MEMORY_PATH")
    notes_path: str = Field(default="memory/notes.json", alias="NOTES_PATH")

    # -------------------------
    # Weather
    # -------------------------
    default_city: str = Field(
        default="Kharagpur",
        alias="DEFAULT_CITY",
    )

    default_country: str = Field(
        default="India",
        alias="DEFAULT_COUNTRY", 
    )


settings = Settings()
