from shared.parameters import LimitOffsetParamDto
from sqlalchemy import select, update
from sqlalchemy.dialects.postgresql import insert, Insert
from sqlalchemy.ext.asyncio import AsyncSession

from ...entity.lead import Lead
from ...schema.external import ExternalLeadResponseDto


class LeadRepository:

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_lead(self, *, lead_id: int):
        query = select(Lead).where(Lead.id == lead_id)
        result = await self.session.scalar(query)
        return result

    async def get_lead_list(self, *, params: LimitOffsetParamDto | None):
        query = select(Lead)

        if params is not None:
            query = query.limit(params.limit).offset(params.offset)
        result = await self.session.execute(query)
        return result.unique().scalars().all()

    async def set_lead_status(self, lead_id: int, status_id: int):
        query = update(Lead).where(Lead.id == lead_id).values({
            "status_id": status_id,
        })
        await self.session.execute(query)
        await self.session.commit()
        return None

    @staticmethod
    def _prepare_insert_object(lead: ExternalLeadResponseDto):
        obj = {
            "id": lead.id,
            "name": lead.name,
            "price": lead.price,
            "responsible_user_id": lead.responsible_user_id,
            "group_id": lead.group_id,
            "status_id": lead.status_id,
            "pipeline_id": lead.pipeline_id,
            "loss_reason_id": lead.loss_reason_id,
            "source_id": lead.source_id,
            "created_by": lead.created_by,
            "updated_by": lead.updated_by,
            "closed_at": lead.closed_at,
            "created_at": lead.created_at,
            "updated_at": lead.updated_at,
            "is_deleted": lead.is_deleted,
            "account_id": lead.account_id,
            "order_code": lead.order_code,
            "primary_lead_id": lead.primary_lead_id,
        }
        return obj

    @staticmethod
    def _prepare_on_conflict_do_update_object(query: Insert):
        obj = {
            "name": query.excluded.name,
            "price": query.excluded.price,
            "responsible_user_id": query.excluded.responsible_user_id,
            "group_id": query.excluded.group_id,
            "status_id": query.excluded.status_id,
            "pipeline_id": query.excluded.pipeline_id,
            "loss_reason_id": query.excluded.loss_reason_id,
            "source_id": query.excluded.source_id,
            "created_by": query.excluded.created_by,
            "updated_by": query.excluded.updated_by,
            "closed_at": query.excluded.closed_at,
            "created_at": query.excluded.created_at,
            "updated_at": query.excluded.updated_at,
            "is_deleted": query.excluded.is_deleted,
            "account_id": query.excluded.account_id,
            "order_code": query.excluded.order_code,
            "primary_lead_id": query.excluded.primary_lead_id,
        }
        return obj

    async def bulk_upsert_lead_list(self, leads: list[ExternalLeadResponseDto]):
        query = insert(Lead).values([
            self._prepare_insert_object(lead) for lead in leads
        ])
        query = query.on_conflict_do_update(
            constraint="amo_leads_pkey",
            set_=self._prepare_on_conflict_do_update_object(query),
        )
        await self.session.execute(query)
        await self.session.commit()
        return None

    async def upsert_lead(self, lead: ExternalLeadResponseDto):
        query = insert(Lead).values([self._prepare_insert_object(lead)])
        query = query.on_conflict_do_update(
            constraint="amo_leads_pkey",
            set_=self._prepare_on_conflict_do_update_object(query),
        )
        query = query.returning(Lead)
        lead = await self.session.scalar(query)
        await self.session.commit()
        return lead
