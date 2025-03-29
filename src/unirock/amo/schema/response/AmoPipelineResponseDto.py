from pydantic import BaseModel, ConfigDict, Field, RootModel, TypeAdapter

from .AmoStatusMinimalResponseDto import AmoStatusMinimalResponseDto


class AmoPipelineResponseDto(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    sort_key: int
    is_main: bool
    is_unsorted_on: bool
    is_archive: bool
    account_id: int
    statuses: list[AmoStatusMinimalResponseDto] = Field(default_factory=list)


AmoPipelineListResponseDto = TypeAdapter(list[AmoPipelineResponseDto])
