from contextlib import asynccontextmanager

import amo.api.v1 as amo
from fastapi import FastAPI
from shared.logger import listener


def register_routers(fastapi_app: FastAPI):
    fastapi_app.include_router(amo.router)


@asynccontextmanager
async def lifespan(fastapi_app: FastAPI):
    listener.start()
    yield
    listener.stop()


app = FastAPI(lifespan=lifespan)
register_routers(app)
