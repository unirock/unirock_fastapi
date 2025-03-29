from shared.parameters import LimitOffsetParamDto
from sqlalchemy.ext.asyncio import AsyncSession

from ...repository import StatusRepository
from ...schema.external import ExternalStatusResponseDto
from ...schema.response import (AmoPipelineListResponseDto,
                                AmoPipelineResponseDto)


class InternalStatusService:

    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session
        self.status_repository = StatusRepository(db_session)

    async def bulk_upsert_status_list(self, statuses: list[ExternalStatusResponseDto]):
        await self.status_repository.bulk_upsert_status_list(statuses)
        return None
