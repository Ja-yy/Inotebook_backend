from typing import Generic, Type, Union, Dict, Any

from fastapi.encoders import jsonable_encoder
from motor.motor_asyncio import AsyncIOMotorDatabase


from app.db.base import db
from app.core.cutom_types import CreateSchemaType, UpdateSchemaType, SchemaType


class BaseRepository(Generic[SchemaType, CreateSchemaType, UpdateSchemaType]):
    """Basic repository class."""

    schema_model: Type[SchemaType]
    collection_name: str

    def __init__(self) -> None:
        self.collection = db.database[self.collection_name]

    async def create(self, db_obj: CreateSchemaType):
        """insert one record"""
        db_obj_in = db_obj.model_dump()
        result = await self.collection.insert_one(db_obj_in)
        return  result.inserted_id
