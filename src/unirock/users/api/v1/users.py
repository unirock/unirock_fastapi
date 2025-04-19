from fastapi import APIRouter
from users.client.keycloak_admin_client import KeycloakAdminClient
from users.service.users import KeycloakUserService
from users.schema import KeycloakUserCreateDto, KeycloakUserDto

router = APIRouter()


@router.post("/")
async def create_user(client: KeycloakAdminClient, user: KeycloakUserCreateDto) -> KeycloakUserDto:
    service = KeycloakUserService(client)
    created_user = await service.create_user(user)
    return created_user

@router.get("/")
async def get_user_list(client: KeycloakAdminClient):
    service = KeycloakUserService(client)
    users = await service.get_user_list()
    return users
