"""ENDPOINT - USER
Endpoints for user signin and signup
"""


from fastapi import APIRouter

from app.models.user import SignUpRes, UserCreate, UserSignin, UserSigninRes
from app.repository.user import UserRepository
from app.utils.auth.auth_barare import JWTUtils
from app.utils.auth.auth_utils import AuthUtils
from app.utils.custom_exception import *

router = APIRouter(prefix="/auth", tags=["Auth"])


# Create a user using : POST "api/auth"
@router.post(
    "/signup",
    responses=get_exception_responses(AlreadyExistsException),
    response_model=SignUpRes,
)
async def signup(new_user: UserCreate):
    """
    Registers a new user by providing user registration information.

    Args:
        new_user (UserCreate): The user registration data.

    Returns:
        SignUpRes: Information about the newly registered user.

    Raises:
        AlreadyExistsException: If a user with the same email already exists.
    """

    db = UserRepository()
    hashed_pass = AuthUtils.get_password_hash(new_user.password)
    new_user.password = hashed_pass
    return await db.create(new_user)


# Login and get access token : POST "api/auth/signin"
@router.post(
    "/signin",
    response_model=UserSigninRes,
)
async def signin(user_data: UserSignin):
    """
    Authenticates a user and generates an access token upon successful login.

    Args:
        user_data (UserSignin): User login data containing email and password.

    Returns:
        UserSigninRes: Information about the authenticated user, including the access token.

    Note:
        This endpoint is used for user login and token generation.
    """

    db = UserRepository()
    user = await AuthUtils.authenticate_user(db, user_data.email, user_data.password)
    access_token = JWTUtils.signJWT(user.get("user_id"))
    return {
        "user_id": user.get("user_id"),
        "email": user.get("email"),
        "access_token": access_token,
        "token_type": "bearer",
    }
