from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    CACHE_HOST: str | None = "redis://localhost:6372"

    model_config = SettingsConfigDict(env_file=".env")