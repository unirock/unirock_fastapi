from keycloak import KeycloakAdmin
from keycloak import KeycloakOpenIDConnection

from users.config import KeycloakClientConfig

config = KeycloakClientConfig()

keycloak_connection = KeycloakOpenIDConnection(
    server_url=config.server_url.encoded_string(),
    username=config.username,
    password=config.password.get_secret_value(),
    realm_name=config.realm_name,
    user_realm_name=config.user_realm_name,
    client_id=config.client_id,
    client_secret_key=config.client_secret_key.get_secret_value(),
    verify=config.verify_ssl
)
