from pydantic import BaseModel, Field, RootModel

from .ExternalLeadResponseDto import ExternalLeadResponseDto


class LeadStatusChangeOrUpdateDto(ExternalLeadResponseDto, BaseModel):
    old_status_id: int

# TODO Доописать

class ExternalWebhookLeadAction(BaseModel):
    status: dict[str, LeadStatusChangeOrUpdateDto] | None = None
    add: dict[str, ExternalLeadResponseDto] | None = None
    delete: ExternalLeadResponseDto | None = None
    update: list[LeadStatusChangeOrUpdateDto] | None = None
    note: None = None
    responsible: None = None
    restore: None = None


class ExternalWebhookLeadEventDto(BaseModel):
    leads: ExternalWebhookLeadAction


class ExternalWebhookEventDto(RootModel):
    root: ExternalWebhookLeadEventDto
