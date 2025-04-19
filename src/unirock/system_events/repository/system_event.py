from datetime import date

from shared.repository.database import AbstractDatabaseRepository
from sqlalchemy import delete
from sqlalchemy.dialects.postgresql import insert

from ..entity import SystemEvent
from ..schema import SystemEventCreateDto


class SystemEventRepository(AbstractDatabaseRepository):

    async def create(self, create_dto: SystemEventCreateDto) -> SystemEvent:
        new_object: SystemEvent = create_dto.to_db_object(SystemEvent)
        # query = insert(SystemEvent).values(new_object).returning(SystemEvent)
        # created_event = await self.session.scalar(query)
        # await self.session.commit()
        # return created_event


    async def vacuum(self, to_date: date):
        query = delete(SystemEvent).where(SystemEvent.timestamp < to_date)
        await self.session.execute(query)
        return None