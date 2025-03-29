from typing import Annotated

import httpx
from fastapi import Depends
from httpx_limiter import AsyncRateLimitedTransport

from ..settings import AmoSettings
from .auth import ApiKeyAuth

settings = AmoSettings()
_client: httpx.AsyncClient | None = None


async def get_amo_client():
    global settings, _client
    if not _client:
        auth = ApiKeyAuth(settings.api_key.get_secret_value())
        httpx_limiter = AsyncRateLimitedTransport.create(rate=6, capacity=6)
        _client = httpx.AsyncClient(
            base_url=settings.base_url,
            auth=auth,
            transport=httpx_limiter,
        )

    return _client


AmoClient = Annotated[httpx.AsyncClient, Depends(get_amo_client)]
