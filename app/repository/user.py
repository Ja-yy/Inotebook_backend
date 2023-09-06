"""REPOSITORIES - USER
User repositores for database operations
"""

from app.core.cutom_types import CreateSchemaType
from app.models.user import User, UserBase
from app.repository.base import BaseRepository
from app.utils.custom_exception import AlreadyExistsException


class UserRepository(BaseRepository):
    schema_model = User
    collection_name = "userCol"

    async def create(self, db_obj: CreateSchemaType):
        user_fill = await self.filter({"email": db_obj.email})
        if user_fill:
            raise AlreadyExistsException(
                identifier=db_obj.email, message="The user already exists"
            )
        return await super().create(db_obj)

    async def get_user_by_email(self, email: str):
        cursor = await self.collection.find_one({"email": email})
        return UserBase(**cursor).model_dump()
