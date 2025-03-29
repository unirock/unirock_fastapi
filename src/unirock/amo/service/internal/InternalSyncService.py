import asyncio

from amo import AmoClient
from sqlalchemy.ext.asyncio import AsyncSession

from ..external.ExternalLeadService import ExternalLeadService
from ..external.ExternalPipelineService import ExternalPipelineService
from . import (InternalLeadService, InternalPipelineService,
               InternalStatusService)


class InternalSyncService:

    def __init__(self, db_session: AsyncSession, amo_client: AmoClient):
        self.pipeline_service = InternalPipelineService(db_session=db_session)
        self.status_service = InternalStatusService(db_session=db_session)
        self.lead_service = InternalLeadService(db_session=db_session)

        self.external_pipeline_service = ExternalPipelineService(amo_client=amo_client)
        self.external_lead_service = ExternalLeadService(amo_client=amo_client)

    async def sync_pipelines_and_statuses(self):
        pipelines = await self.external_pipeline_service.get_pipelines()
        await self.pipeline_service.bulk_upsert_pipeline_list(pipelines)
        status_list = []
        for pipeline in pipelines:
            status_list.extend(pipeline.statuses)
        await self.status_service.bulk_upsert_status_list(status_list)
        pipelines = await self.pipeline_service.get_pipeline_list(limit_offset_params=None)
        return pipelines

    async def sync_leads(self):
        page = 1
        limit = 250
        while True:
            leads_page = await self.external_lead_service.get_leads_page(page, limit)
            await self.lead_service.bulk_upsert_lead_list(leads_page.embedded["leads"])

            next_page = leads_page.links.next
            if next_page is None:
                break
            else:
                page += 1
            await asyncio.sleep(1)