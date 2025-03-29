from enum import StrEnum
from pathlib import Path

from pydantic import computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict


class EnvType(StrEnum):
    DEV = "dev"
    PROD = "prod"


class App(BaseSettings):
    environment: EnvType = EnvType.DEV


class RedisSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="redis_")
    url: str


class PostgresSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="postgres_")

    host: str
    port: int
    user: str
    password: str
    db: str

    @computed_field
    @property
    def dsn(self) -> str:
        host = self.host
        port = self.port
        user = self.user
        password = self.password
        db = self.db
        return f"postgresql+asyncpg://{user}:{password}@{host}:{port}/{db}"
