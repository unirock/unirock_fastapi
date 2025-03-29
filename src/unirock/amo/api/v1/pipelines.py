from amo.schema.response import AmoPipelineResponseDto
from amo.service import InternalPipelineService
from fastapi import APIRouter
from shared.repository.database.connection import AsyncDBSession

router = APIRouter()


@router.get("/")
async def get_pipeline_list(db_session: AsyncDBSession) -> list[AmoPipelineResponseDto]:
    pipelines = await InternalPipelineService(db_session).get_pipeline_list(limit_offset_params=None)
    return pipelines


@router.get("/{pipeline_id}")
async def get_pipeline(db_session: AsyncDBSession, pipeline_id: int) -> AmoPipelineResponseDto:
    pipeline = await InternalPipelineService(db_session).get_pipeline(pipeline_id=pipeline_id)
    return pipeline


