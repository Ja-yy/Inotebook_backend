"""ENDPOINT - NOTES
Endpoints for notes 
"""

from fastapi import APIRouter

router = APIRouter(prefix="/notes", tags=["Notes"])


@router.get("/")
async def get_all_notes():
    return ...
