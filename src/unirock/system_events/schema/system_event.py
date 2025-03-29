from pydantic import BaseModel, ConfigDict
from shared.schema import MappableSchema


class SystemEventCreateDto(MappableSchema, BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: str
    app: str
    type: str
    event_data: dict
