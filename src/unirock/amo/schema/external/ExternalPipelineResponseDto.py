from typing import Literal

from pydantic import BaseModel, Field, RootModel, TypeAdapter, computed_field

from .ExternalStatusResponseDto import ExternalStatusResponseDto
from .generic import AmoListResponseGenericDto


class ExternalPipelineResponseDto(BaseModel):
    id: int
    name: str
    sort_key: int = Field(alias="sort")
    is_main: bool
    is_unsorted_on: bool
    is_archive: bool
    account_id: int
    embedded: dict[Literal["statuses"], list[ExternalStatusResponseDto]] = Field(alias="_embedded")

    @computed_field
    @property
    def statuses(self) -> list[ExternalStatusResponseDto]:
        return self.embedded["statuses"]


ExternalPipelineListResponseDto = RootModel[list[ExternalPipelineResponseDto]]

ExternalPipelineListPageResponseDto = TypeAdapter(
    AmoListResponseGenericDto[ExternalPipelineResponseDto, Literal["pipelines"]])
