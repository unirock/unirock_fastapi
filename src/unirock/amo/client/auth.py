import httpx
import redis.asyncio as redis
from httpx import Auth
from yarl import URL


class ApiKeyAuth(Auth):

    def __init__(self, api_key: str):
        self.api_key = api_key

    async def async_auth_flow(self, request: httpx.Request):
        request.headers["Authorization"] = f"Bearer {self.api_key}"
        yield request
