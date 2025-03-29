from fastapi import APIRouter

from . import pipelines, sync, webhook, leads

router = APIRouter(prefix="/amo", tags=["amo"])
router.include_router(pipelines.router, prefix="/pipelines")
router.include_router(sync.router, prefix="/sync")
router.include_router(webhook.router, prefix="/webhook")
router.include_router(leads.router, prefix="/leads")


