from contextlib import asynccontextmanager
from typing import AsyncGenerator

import redis.asyncio as redis
from settings import RedisSettings

POOL: redis.ConnectionPool | None = None


def init_pool():
    global POOL
    if not POOL:
        settings = RedisSettings()
        POOL = redis.ConnectionPool.from_url(settings.url)


async def close_pool():
    global POOL
    if POOL:
        await POOL.aclose()


async def get_client():
    global POOL
    if POOL is None:
        raise ValueError("Пул соединений с redis не инициализирован")
    client = redis.Redis.from_pool(POOL)
    yield client
    await client.aclose()
