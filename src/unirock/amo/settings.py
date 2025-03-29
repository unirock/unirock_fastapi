from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class AmoSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="amo_")

    api_key: SecretStr
    base_url: str
