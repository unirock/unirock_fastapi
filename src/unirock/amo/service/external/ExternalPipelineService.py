from amo import AmoClient
from sqlalchemy.ext.asyncio import AsyncSession

from ...repository.external.pipeline import AmoPipelineRepository


class ExternalPipelineService:

    def __init__(self, amo_client: AmoClient):
        self.repository = AmoPipelineRepository(amo_client)

    async def get_pipelines(self):
        return await self.repository.get_pipeline_list()
