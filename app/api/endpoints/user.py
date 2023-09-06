"""ENDPOINT - USER
Endpoints for user signin and signup
"""

from fastapi import APIRouter

from app.models.user import SignUpResponse, UserCreate, UserSignin, UserSigninResponse
from app.repository.user import UserRepository
from app.utils.auth.auth_barare import JWTUtils
from app.utils.auth.auth_utils import AuthUtils
from app.utils.custom_exception import *

router = APIRouter(prefix="/auth", tags=["auth"])


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
    access_token = JWTUtils.signJWT(user.get("email"))
    return {
        "user": user.get("email"),
        "access_token": access_token,
        "token_type": "bearer",
    }
