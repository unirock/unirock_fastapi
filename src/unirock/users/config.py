from pydantic import HttpUrl, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class KeycloakClientConfig(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="keycloak_")

    server_url: HttpUrl
    username: str
    password: SecretStr

    realm_name: str
    user_realm_name: str | None = None

    client_id: str
    client_secret_key: SecretStr
    verify_ssl: bool = True
