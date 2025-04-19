from fastapi import APIRouter

from . import pipelines, sync, webhook, leads

router = APIRouter(prefix="/amo", tags=["amo"])
router.include_router(pipelines.router)
router.include_router(sync.router)
router.include_router(webhook.router)
router.include_router(leads.router)
