import asyncio
from sqlalchemy.ext.asyncio import AsyncSession

from . import InternalLeadService
from ...schema.external.ExternalWebhookEventDto import ExternalWebhookEventDto, ExternalWebhookLeadEventDto

from shared.broker import broker
from shared.clients.database import AsyncDBSession


class InternalAmoLeadEventService:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session
        self.lead_service = InternalLeadService(db_session)

    async def process_update(self, webhook: ExternalWebhookLeadEventDto):
        leads = webhook.leads.update
        coros = (self.lead_service.update_lead(lead) for lead in leads.values())
        await asyncio.gather(*coros)

    async def process_status_update(self, webhook: ExternalWebhookLeadEventDto):
        leads = webhook.leads.status
        coros = (self.lead_service.set_lead_status(lead.id, lead.status_id) for lead in leads.values())
        await asyncio.gather(*coros)

    async def process_create(self, webhook: ExternalWebhookLeadEventDto):
        leads = webhook.leads.add
        coros = (self.lead_service.create_lead(lead) for lead in leads.values())
        await asyncio.gather(*coros)

    async def process_delete(self, webhook: ExternalWebhookLeadEventDto):
        leads = webhook.leads.delete
        ...

    async def process_webhook(self, webhook_content: ExternalWebhookEventDto):
        content = webhook_content.root.leads
        if content.update:
            await self.process_update(webhook_content.root)
        elif content.status:
            await self.process_status_update(webhook_content.root)
        elif content.create:
            await self.process_create(webhook_content.root)


@broker.subscriber(stream="amo_webhooks")
async def handle_webhook(webhook: ExternalWebhookEventDto, db_session: AsyncDBSession):
    await InternalAmoLeadEventService(db_session).process_webhook(webhook)
