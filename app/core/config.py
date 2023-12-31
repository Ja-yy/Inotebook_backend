"""SETTINGS
Settings loaders using Pydantic BaseSettings classes (load from environment variables / dotenv file)
"""

from typing import List

from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

# Load environment variables from .env file
load_dotenv()


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file="dev.env", env_file_encoding="utf-8")

    DATABASE_URL: str
    DATABASE_COLLECTION: str
    DATABASE_NAME: str

    CORS_ORIGINS: List[str]
    CORS_ALLOW_CREDENTIALS: bool
    CORS_ALLOW_METHODS: List[str]
    CORS_ALLOW_HEADERS: List[str]

    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str
    JWT_ACCESS_TOKEN_EXPIRE_HOURS: int


settings = Settings()
