from fastapi import APIRouter

from . import users

router = APIRouter(prefix="/users", tags=["users"])
router.include_router(users.router)
