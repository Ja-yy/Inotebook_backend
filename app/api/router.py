from fastapi import APIRouter

from app.api.endpoints import notes, user

router = APIRouter(prefix="/api/v1")


router.include_router(user.router)
router.include_router(notes.router)
