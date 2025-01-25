import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()


class Settings(BaseSettings):

    weather_api_key: str = os.getenv("WEATHER_API_KEY")
    weather_api_base_url: str = os.getenv(
        "WEATHER_API_BASE_URL", "http://api.weatherapi.com/v1"
    )
    database_url: str = "sqlite:///./cities_temperature.db"
    app_name: str = "City Temperature Management API"
    app_version: str = "0.1.0"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


def get_settings() -> Settings:
    return Settings()
