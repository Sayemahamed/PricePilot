from pydantic_settings import BaseSettings, SettingsConfigDict

"""
This module contains the configuration settings for the API.
"""


class Settings(BaseSettings):
    REDIS_URL: str
    POSTGRES_URL_ASYNC: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    OPENAI_API_KEY: str

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )


settings = Settings()  # type:ignore
