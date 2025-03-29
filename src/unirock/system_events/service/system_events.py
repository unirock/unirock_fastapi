from datetime import date
from uuid import UUID

from shared.service.abstract_service import DBService
from sqlalchemy.ext.asyncio import AsyncSession

from ..entity.app_events import SystemEvent
from ..repository.system_event import SystemEventRepository
from ..schema import SystemEventCreateDto


class SystemEventService(DBService):

    def __init__(self, db_session: AsyncSession):
        super().__init__(db_session)
        self.event_repository: SystemEventRepository = SystemEventRepository(db_session)

    async def vacuum_events(self, to_date: date) -> None:
        await self.event_repository.vacuum(to_date)
        # logger.info(f"События до {to_date.strftime("%d.%m.%Y")} были удалены")
        return None

    async def create(self, create_dto: SystemEventCreateDto) -> SystemEvent:
        created_event = await self.event_repository.create(create_dto)
        return created_event

    async def read(self):
        ...

    async def read_list(self):
        ...
