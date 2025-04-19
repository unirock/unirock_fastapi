from keycloak import KeycloakAdmin
from users.schema.users import KeycloakUserCreateDto, KeycloakUserDto
from users.repository.external.users import KeycloakUserRepository


class KeycloakUserService:

    def __init__(self, client: KeycloakAdmin):
        self.repository = KeycloakUserRepository(client)

    async def create_user(self, user: KeycloakUserCreateDto) -> KeycloakUserDto:
        user_id = await self.repository.create_user(user)
        user_dto = KeycloakUserDto(
            id=user_id,
            first_name=user.first_name,
            family_name=user.family_name,
            patronymic=user.patronymic,
            email=user.email,
            phone_number=user.phone_number,
            avatar_url=user.avatar_url,
        )
        return user_dto

    async def get_user_list(self) -> list[KeycloakUserDto]:
        return await self.repository.get_user_list()

    async def get_user(self, user_id: str) -> KeycloakUserDto:
        ...
