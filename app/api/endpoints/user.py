"""ENDPOINT - USER
Endpoints for user signin and signup
"""

from typing import Annotated, Dict

from fastapi import APIRouter, Depends

from app.models.user import SignUpResponse, UserCreate, UserSignin, UserSigninResponse
from app.repository.user import UserRepository
from app.utils.auth.auth_barare import JWTBearer, JWTUtils
from app.utils.auth.auth_utils import AuthUtils
from app.utils.custom_exception import *

router = APIRouter(prefix="/auth", tags=["Auth"])


# Create a user using : POST "api/auth"
@router.post(
    "/signup",
    responses=get_exception_responses(AlreadyExistsException),
    response_model=SignUpResponse,
)
async def signup(new_user: UserCreate):
    db = UserRepository()
    hashed_pass = AuthUtils.get_password_hash(new_user.password)
    new_user.password = hashed_pass
    return await db.create(new_user)


# Login and get access token : POST "api/auth/signin"
@router.post(
    "/signin",
    response_model=UserSigninResponse,
)
async def signin(user_data: UserSignin):
    db = UserRepository()
    user = await AuthUtils.authenticate_user(db, user_data.email, user_data.password)
    access_token = JWTUtils.signJWT(user.get("_id"))
    return {
        "id": user.get("id"),
        "email": user.get("email"),
        "access_token": access_token,
        "token_type": "bearer",
    }


@router.get(
    "/getuser",
)
async def get_user_detail(tt: Annotated[Dict, Depends(JWTBearer())]):
    return {"ping": tt}
