from uuid import UUID

from keycloak import KeycloakAdmin

from users.schema.users import KeycloakUserCreateDto


class KeycloakUserRepository:

    def __init__(self, client: KeycloakAdmin):
        self.client = client

    # Вернёт всегда всех, потому что сейчас пользователи только внутренние
    async def get_user_list(self):
        return await self.client.a_get_users(query={
            "briefRepresentation": True
        })

    async def get_user(self, user_id: UUID):
        return await self.client.a_get_user(str(user_id), user_profile_metadata=True)

    async def create_user(self, user: KeycloakUserCreateDto) -> UUID:
        user_obj = {
            "email": user.email,
            "username": user.username,
            "enabled": True,
            "firstName": user.first_name,
            "lastName": user.family_name,
            "attributes": {
                "patronymic": user.patronymic,
            },
        }
        user_id = await self.client.a_create_user(user_obj, exist_ok=False)
        return UUID(user_id)

    async def set_password(self, user_id: UUID, password: str):
        return await self.client.a_set_user_password(str(user_id), password, temporary=True)
