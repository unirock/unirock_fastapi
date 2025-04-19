from contextlib import asynccontextmanager

import amo.api.v1 as amo
import users.api.v1 as users
from fastapi import FastAPI
from shared.logger import listener
from shared.clients import database
from shared.broker import broker
from middleware.auth import authorization_middleware

ROUTERS = [amo.router, users.router]

MIDDLEWARES = [authorization_middleware]


def register_routers(fastapi_app: FastAPI):
    global ROUTERS
    for router in ROUTERS:
        fastapi_app.include_router(router)


def register_middleware(fastapi_app: FastAPI):
    global MIDDLEWARES
    for middleware in MIDDLEWARES:
        fastapi_app.add_middleware(middleware)


@asynccontextmanager
async def lifespan(_: FastAPI):
    await broker.connect()
    listener.start()
    yield
    await broker.close()
    listener.stop()


app = FastAPI(lifespan=lifespan)
register_routers(app)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
