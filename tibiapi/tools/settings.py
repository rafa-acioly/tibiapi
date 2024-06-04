from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    CACHE_HOST: str | None = "redis://localhost:6372"
    SENTRY_DSN: str | None = None
    CACHE_ENV: str = "TEST"

    model_config = SettingsConfigDict(env_file=".env")
