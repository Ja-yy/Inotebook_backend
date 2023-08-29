from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from app.schemas.user import User

from app.repository.user import UserRepository

router = APIRouter(prefix="/api/auth", tags=["auth"])


# Create a user using : POST "api/auth"
@router.post("/")
async def signup(new_user: User):
    db = UserRepository()
    result = await db.create(new_user)
    return JSONResponse(str(result))
