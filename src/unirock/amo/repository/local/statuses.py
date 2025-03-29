from shared.parameters import LimitOffsetParamDto
from sqlalchemy import select
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncSession

from ...entity.status import Status
from ...schema.external import ExternalStatusResponseDto


class StatusRepository:

    def __init__(self, session: AsyncSession):
        self.session = session

    async def bulk_upsert_status_list(self, statuses: list[ExternalStatusResponseDto]):
        query = (insert(Status).values([
            {
                "id": status.id,
                "name": status.name,
                "sort_key": status.sort_key,
                "is_editable": status.is_editable,
                "pipeline_id": status.pipeline_id,
                "color": status.color,
                "type": status.type,
                "account_id": status.account_id,
            } for status in statuses
        ]))
        query = query.on_conflict_do_update(
            constraint="amo_statuses_pkey",
            set_={
                "name": query.excluded.name,
                "sort_key": query.excluded.sort_key,
                "is_editable": query.excluded.is_editable,
                "color": query.excluded.color,
                "type": query.excluded.type,
                "account_id": query.excluded.account_id,
            }
        )
        await self.session.execute(query)
        await self.session.commit()
        return None
