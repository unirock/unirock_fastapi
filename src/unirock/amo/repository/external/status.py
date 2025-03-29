# from ... import AmoClient
# from ...schema.external import ExternalPipelineResponseDto, ExternalPipelineListResponseDto
# from ...schema.external.generic import AmoListResponseGenericDto
#
#
# class AmoStatusRepository:
#
#     def __init__(self, client: AmoClient):
#         self.client = client
#
#     async def get_pipeline_list(self) -> list[ExternalPipelineResponseDto]:
#         pipelines_response = await self.client.get("/api/v4/leads/pipelines")
#         return AmoListResponseGenericDto[ExternalPipelineResponseDto].model_validate_json(
#             pipelines_response.content).embedded["pipelines"]
#
#     async def get_pipeline(self, pipeline_id: str) -> ExternalPipelineResponseDto:
#         pipeline_response = await self.client.get(f"/api/v4/leads/pipelines/{pipeline_id}")
#         return ExternalPipelineResponseDto.model_validate_json(pipeline_response.content)
