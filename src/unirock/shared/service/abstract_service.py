from abc import ABC, abstractmethod

from sqlalchemy.ext.asyncio import AsyncSession


class DBService(ABC):

    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session
