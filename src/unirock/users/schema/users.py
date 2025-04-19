import datetime
from functools import partial
from uuid import UUID

from pydantic import BaseModel, EmailStr, Field, AliasPath

AttributePath = partial(AliasPath, "attributes")


class KeycloakUserDto(BaseModel):
    id: UUID
    username: str
    enabled: bool

    first_name: str = Field(alias="firstName")
    family_name: str = Field(alias="lastName")
    patronymic: str | None = Field(None, validation_alias=AttributePath("patronymic"))

    email: EmailStr
    phone_number: str | None = Field(None, validation_alias=AttributePath("phone_number"))

    avatar_url: str | None = Field(None, validation_alias=AttributePath("avatar_url"))

    roles: list[str]

    created_at: datetime.datetime = Field(alias="createdTimestamp")


class KeycloakUserCreateDto(BaseModel):
    username: str

    first_name: str
    family_name: str
    patronymic: str | None

    email: EmailStr
    phone_number: str

    avatar_url: str | None = None
