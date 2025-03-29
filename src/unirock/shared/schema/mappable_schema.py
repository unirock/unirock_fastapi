from typing import Type

from pydantic import BaseModel
from sqlalchemy.orm import DeclarativeBase


class MappableSchema(BaseModel):

    def to_db_object[T: DeclarativeBase](self, model_cls: Type[T]) -> T:
        return model_cls(**self.model_dump())