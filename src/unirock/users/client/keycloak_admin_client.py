from typing import Annotated

from fastapi import Depends
from keycloak import KeycloakAdmin
from users.config import KeycloakClientConfig

# from .keycloak_connection import keycloak_connection

config = KeycloakClientConfig()
# keycloak_admin = KeycloakAdmin(connection=keycloak_connection)
keycloak_admin = KeycloakAdmin(
    server_url=config.server_url.encoded_string(),
    username=config.username,
    password=config.password.get_secret_value(),
    realm_name=config.realm_name,
    user_realm_name=config.user_realm_name,
)


async def get_client():
    return keycloak_admin


KeycloakAdminClient = Annotated[KeycloakAdmin, Depends(get_client)]
