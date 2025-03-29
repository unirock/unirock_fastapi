from amo.schema.response import AmoLeadResponseDto
from fastapi import APIRouter, Depends

from amo.service import InternalLeadService
from shared.parameters import LimitOffsetParams
from shared.repository.database.connection import AsyncDBSession

router = APIRouter()


@router.get("/")
async def get_lead_list(
        db_session: AsyncDBSession,
        limit_offset_params: LimitOffsetParams,
        query: str | None = None,
) -> list[AmoLeadResponseDto]:
    print(limit_offset_params)
    return []
    leads = await InternalLeadService(db_session).get_lead_list(limit_offset_params=limit_offset_params, query=query)
    return leads


@router.get("/{lead_id}")
async def get_lead(db_session: AsyncDBSession, lead_id: int) -> AmoLeadResponseDto:
    lead = await InternalLeadService(db_session).get_lead(lead_id=lead_id)
    return lead

