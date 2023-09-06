"""REPOSITORIES
Methods to interact with the database
"""

from datetime import datetime
from typing import Any, Dict, Generic, List, Type, Union

from app.core.cutom_types import CreateSchemaType, SchemaType, UpdateSchemaType
from app.db.base import db
from app.utils.custom_exception import NotFoundException


class BaseRepository(Generic[SchemaType, CreateSchemaType, UpdateSchemaType]):
    """Basic repository class."""

    schema_model: Type[SchemaType]
    collection_name: str

    def __init__(self) -> None:
        self.collection = db.database[self.collection_name]

    async def get(self, _id: str):
        """Retrieve a single record by its unique id"""
        document = await self.collection.find_one({"_id": _id})
        if not document:
            raise NotFoundException(_id)
        return document

    async def create(self, db_obj: CreateSchemaType):
        """insert one record"""
        db_obj_in = db_obj.model_dump()
        db_obj_in["created_at"] = datetime.utcnow()
        result = await self.collection.insert_one(db_obj_in)
        assert result.acknowledged

        return await self.get(result.inserted_id)

    async def filter(
        self, filters: Dict[str, Any] = None, projection: List[str] = None
    ) -> Union[List[dict], List[Union[dict, Any]]]:
        """Filter records based on given parameters and return selected fields from MongoDB."""

        if projection is None:
            projection = {}

        cursor = self.collection.find(filters, projection=projection)

        results = []
        async for document in cursor:
            results.append(document)
        return results
