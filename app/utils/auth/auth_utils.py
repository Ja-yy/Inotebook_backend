"""UTILS - AUTH
Utility functions for authentication
"""

from typing import Dict

from passlib.context import CryptContext

from app.repository.user import UserRepository
from app.utils.custom_exception import NotFoundException, WrongLoginDetialException


class AuthUtils:
    pwd_context: CryptContext = CryptContext(schemes=["bcrypt"], deprecated="auto")

    @classmethod
    def get_password_hash(cls, password):
        return cls.pwd_context.hash(password)

    @classmethod
    async def authenticate_user(cls, db: UserRepository, email: str, password: str):
        def verify_password(plain_password, hashed_password):
            return cls.pwd_context.verify(plain_password, hashed_password)

        user: Dict = await db.get_user_by_email(email)
        if not user:
            raise NotFoundException(identifier=email, message="User not found")
        if not verify_password(
            plain_password=password, hashed_password=user.get("password")
        ):
            raise WrongLoginDetialException(identifier=email)
        return user
