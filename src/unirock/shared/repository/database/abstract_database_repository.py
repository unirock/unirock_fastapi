from abc import ABC

from sqlalchemy.ext.asyncio import AsyncSession


class AbstractDatabaseRepository(ABC):

    def __init__(self, db_session: AsyncSession):
        self.session = db_session

    async def commit(self):
        await self.session.commit()
