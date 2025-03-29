from amo import AmoClient
from amo.schema.response import AmoPipelineResponseDto
from amo.service import InternalSyncService
from fastapi import APIRouter
from shared.repository.database.connection import AsyncDBSession

router = APIRouter()


@router.post(
    "/pipelines_and_statuses",
    name="синхронизировать воронки + статусы",
    description="Выдернем воронки и статусы из Амо и сохраним их локально"
)
async def sync_pipelines_and_statuses(
        db_session: AsyncDBSession,
        amo_client: AmoClient
) -> list[AmoPipelineResponseDto]:
    pipelines = await InternalSyncService(db_session=db_session, amo_client=amo_client).sync_pipelines_and_statuses()
    return pipelines

@router.post("/leads")
async def sync_leads(
        db_session: AsyncDBSession,
        amo_client: AmoClient
):
    leads = await InternalSyncService(db_session=db_session, amo_client=amo_client).sync_leads()
    return leads