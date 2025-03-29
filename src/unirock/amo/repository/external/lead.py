from typing import Literal

from ... import AmoClient
from ...schema.external import (ExternalLeadListPageResponseDto,
                                ExternalLeadResponseDto)
from ...schema.external.generic import AmoListResponseGenericDto


class AmoLeadRepository:

    def __init__(self, client: AmoClient):
        self.client = client

    async def get_leads_page(self, page: int, limit: int) -> AmoListResponseGenericDto[
        ExternalLeadResponseDto, Literal["leads"]]:
        if limit > 250:
            limit = 250
        leads_response = await self.client.get("/api/v4/leads",
                                               params={"page": page, "limit": limit})
        leads_page = ExternalLeadListPageResponseDto.validate_json(leads_response.content)
        return leads_page

    async def get_lead(self, lead_id: str) -> ExternalLeadResponseDto:
        lead_response = await self.client.get(f"/api/v4/leads/{lead_id}")
        return ExternalLeadResponseDto.model_validate_json(lead_response.content)
