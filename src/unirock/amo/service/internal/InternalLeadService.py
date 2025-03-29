from shared.parameters import LimitOffsetParamDto
from sqlalchemy import Result
from sqlalchemy.ext.asyncio import AsyncSession

from ...repository import PipelineRepository
from ...repository.local.leads import LeadRepository
from ...schema.external import (ExternalLeadResponseDto,
                                ExternalPipelineResponseDto)
from ...schema.response import (AmoPipelineListResponseDto,
                                AmoPipelineResponseDto,
                                AmoStatusMinimalResponseDto, AmoLeadResponseDto)


class InternalLeadService:

    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session
        self.lead_repository = LeadRepository(db_session)

    async def bulk_upsert_lead_list(self, leads: list[ExternalLeadResponseDto]) -> None:
        await self.lead_repository.bulk_upsert_lead_list(leads)
        return None

    async def upsert_lead(self, lead: ExternalLeadResponseDto) -> AmoLeadResponseDto:
        lead = await self.lead_repository.upsert_lead(lead)
        return AmoLeadResponseDto.model_validate(lead)

    async def set_lead_status(self, lead_id: int, status_id: int):
        await self.lead_repository.set_lead_status(lead_id, status_id)
        return None


    async def get_lead_list(self,
                            query: str,
                            limit_offset_params: LimitOffsetParamDto | None
    ) -> list[AmoLeadResponseDto]:
        ...

    async def get_lead(self, lead_id: int) -> AmoLeadResponseDto:
        ...
