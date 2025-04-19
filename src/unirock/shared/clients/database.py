from typing import Annotated

from fastapi import Depends
from settings import PostgresSettings
from sqlalchemy import pool
from sqlalchemy.ext.asyncio import (AsyncSession, async_sessionmaker,
                                    create_async_engine)

config = PostgresSettings()
engine = create_async_engine(config.dsn, poolclass=pool.NullPool)
session_factory = async_sessionmaker(bind=engine)

async def get_connection() -> AsyncSession:
    global session_factory
    async with session_factory() as session:
        yield session


AsyncDBSession = Annotated[AsyncSession, Depends(get_connection)]