from pydantic import BaseModel, Field


class ExternalStatusResponseDto(BaseModel):
    id: int
    name: str
    sort_key: int = Field(alias="sort")
    is_editable: bool
    pipeline_id: int
    color: str
    type: int
    account_id: int
