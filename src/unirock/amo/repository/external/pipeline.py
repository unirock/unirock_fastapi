from typing import Literal

from ... import AmoClient
from ...schema.external import (ExternalPipelineListPageResponseDto,
                                ExternalPipelineResponseDto)
from ...schema.external.generic import AmoListResponseGenericDto


class AmoPipelineRepository:

    def __init__(self, client: AmoClient):
        self.client = client

    async def get_pipeline_list(self) -> list[ExternalPipelineResponseDto]:
        pipelines_response = await self.client.get("/api/v4/leads/pipelines")
        pipelines_page = ExternalPipelineListPageResponseDto.validate_json(pipelines_response.content)
        return pipelines_page.embedded["pipelines"]

    async def get_pipeline(self, pipeline_id: str) -> ExternalPipelineResponseDto:
        pipeline_response = await self.client.get(f"/api/v4/leads/pipelines/{pipeline_id}")
        return ExternalPipelineResponseDto.model_validate_json(pipeline_response.content)
