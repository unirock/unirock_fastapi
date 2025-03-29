import logging

from shared.parameters import LimitOffsetParamDto
from sqlalchemy.ext.asyncio import AsyncSession

from ...logger import amo_logger
from ...repository import PipelineRepository
from ...schema.external import ExternalPipelineResponseDto
from ...schema.response import AmoPipelineListResponseDto, AmoPipelineResponseDto


class InternalPipelineService:

    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session
        self.pipeline_repository = PipelineRepository(db_session)

    async def get_pipeline(self, *, pipeline_id: int) -> AmoPipelineResponseDto | None:
        pipeline = await self.pipeline_repository.get_pipeline(pipeline_id=pipeline_id)
        if pipeline is not None:
            pipeline_dto = AmoPipelineResponseDto.model_validate(pipeline)
            return pipeline_dto

    async def get_pipeline_list(self, limit_offset_params: LimitOffsetParamDto | None) -> list[AmoPipelineResponseDto]:
        result = await self.pipeline_repository.get_pipeline_list(params=limit_offset_params)
        pipeline_list_dto = AmoPipelineListResponseDto.validate_python(result)
        return pipeline_list_dto

    async def bulk_upsert_pipeline_list(self, pipelines: list[ExternalPipelineResponseDto]) -> None:
        await self.pipeline_repository.bulk_upsert_pipeline_list(pipelines)
        return None
