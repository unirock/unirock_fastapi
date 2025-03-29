from shared.parameters import LimitOffsetParamDto
from sqlalchemy import select
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import aliased

from ...entity.pipeline import Pipeline
from ...entity.status import Status
from ...schema.external import ExternalPipelineResponseDto


class PipelineRepository:

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_pipeline(self, *, pipeline_id: int):
        query = select(Pipeline).where(Pipeline.id == pipeline_id)
        result = await self.session.scalar(query)
        return result

    async def get_pipeline_list(self, *, params: LimitOffsetParamDto | None):
        query = select(Pipeline).order_by(Pipeline.sort_key)

        if params is not None:
            query = query.limit(params.limit).offset(params.offset)
        result = await self.session.execute(query)
        return result.unique().scalars().all()

    async def bulk_upsert_pipeline_list(self, pipelines: list[ExternalPipelineResponseDto]):
        query = (insert(Pipeline).values([
            {
                "id": pipeline.id,
                "name": pipeline.name,
                "sort_key": pipeline.sort_key,
                "is_main": pipeline.is_main,
                "is_unsorted_on": pipeline.is_unsorted_on,
                "is_archive": pipeline.is_archive,
                "account_id": pipeline.account_id,
            } for pipeline in pipelines
        ]))
        query = query.on_conflict_do_update(
            constraint="amo_pipelines_pkey",
            set_={
                "name": query.excluded.name,
                "sort_key": query.excluded.sort_key,
                "is_main": query.excluded.is_main,
                "is_unsorted_on": query.excluded.is_unsorted_on,
                "is_archive": query.excluded.is_archive,
                "account_id": query.excluded.account_id,
            }
        )
        await self.session.execute(query)
        await self.session.commit()
        return None
