from pydantic import BaseModel, ConfigDict


class AmoStatusMinimalResponseDto(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    sort_key: int
    is_editable: bool
    pipeline_id: int
    color: str
    type: int
    account_id: int
