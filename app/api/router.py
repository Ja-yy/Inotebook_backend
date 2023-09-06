from fastapi import APIRouter

from app.api.endpoints import user

router = APIRouter(prefix="/api/v1")


router.include_router(user.router)
