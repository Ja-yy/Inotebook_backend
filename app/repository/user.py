from app.repository.base import BaseRepository
from app.schemas.user import User


class UserRepository(BaseRepository):
    schema_model = User
    collection_name = "userCol"


    async def filter():
        ...