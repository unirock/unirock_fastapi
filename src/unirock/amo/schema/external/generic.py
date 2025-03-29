from typing import Any, Literal

from pydantic import BaseModel, Field
from sqlalchemy import alias


class Link(BaseModel):
    href: str


class Links(BaseModel):
    self: Link | None = None
    next: Link | None = None
    first: Link | None = None
    prev: Link | None = None


class AmoListResponseGenericDto[T, EmbeddedTypeName](BaseModel):
    total_items: int | None = Field(None, alias="_total_items")
    links: Links = Field(alias="_links")
    embedded: dict[EmbeddedTypeName, list[T]] = Field(alias='_embedded')
