import datetime
from typing import Any

from pydantic import BaseModel, Field, RootModel, computed_field

from .ExternalLeadResponseDto import ExternalLeadResponseDto


class CustomFieldValue(BaseModel):
    value: Any


class CustomField(BaseModel):
    field_id: int
    field_name: str
    field_code: str | None
    field_type: str
    values: list[CustomFieldValue]


class LeadCreateDto(BaseModel):
    id: int
    name: str
    status_id: int
    price: int
    responsible_user_id: int

    pipeline_id: int
    loss_reason_id: int | None = None
    source_id: int | None = None
    created_by: int = Field(alias='created_user_id')
    updated_by: int | None = None
    created_at: datetime.datetime
    updated_at: datetime.datetime | None = None
    is_deleted: bool = False
    custom_fields_values: list[CustomField] | None = Field(default_factory=list)
    score: int | None = None
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

class LeadDeleteDto(BaseModel):
    id: int
# TODO Доописать

class ExternalWebhookLeadAction(BaseModel):
    status: list[LeadCreateDto] | None = None
    add: list[LeadCreateDto] | None = None
    delete: list[LeadDeleteDto] | None = None
    update: list[LeadCreateDto] | None = None
    note: None = None
    responsible: None = None
    restore: None = None


class ExternalWebhookLeadEventDto(BaseModel):
    leads: ExternalWebhookLeadAction


class ExternalWebhookEventDto(RootModel):
    root: ExternalWebhookLeadEventDto
