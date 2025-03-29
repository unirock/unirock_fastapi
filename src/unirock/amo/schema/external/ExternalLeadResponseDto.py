import datetime
from typing import Any, Literal

from pydantic import BaseModel, Field, RootModel, TypeAdapter, computed_field

from .ExternalStatusResponseDto import ExternalStatusResponseDto
from .generic import AmoListResponseGenericDto


class CustomFieldValue(BaseModel):
    value: Any


class CustomField(BaseModel):
    field_id: int
    field_name: str
    field_code: str | None
    field_type: str
    values: list[CustomFieldValue]


class ExternalLeadResponseDto(BaseModel):
    id: int
    name: str
    price: int
    responsible_user_id: int
    group_id: int
    status_id: int
    pipeline_id: int
    loss_reason_id: int | None
    source_id: int | None = None
    created_by: int
    updated_by: int
    closed_at: datetime.datetime | None
    created_at: datetime.datetime
    updated_at: datetime.datetime
    is_deleted: bool
    custom_fields_values: list[CustomField] | None
    score: int | None
    account_id: int

    def _get_singular_custom_field_value(self, key: str):
        custom_fields = self.custom_fields_values
        if not custom_fields:
            return None
        for field in custom_fields:
            custom_field_key = field.field_name
            if key == custom_field_key:
                if field.values:
                    return field.values[0].value

    @computed_field
    @property
    def order_code(self) -> str | None:
        return self._get_singular_custom_field_value("Номер договора")

    @computed_field
    @property
    def primary_lead_id(self) -> int | None:
        try:
            return int(self._get_singular_custom_field_value("test_id"))
        except (ValueError, TypeError):
            return None


ExternalLeadListResponseDto = RootModel[list[ExternalLeadResponseDto]]

ExternalLeadListPageResponseDto = TypeAdapter(
    AmoListResponseGenericDto[ExternalLeadResponseDto, Literal["leads"]])
