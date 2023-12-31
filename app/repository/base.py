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
        db_obj_in = db_obj.model_dump(by_alias=True)
        db_obj_in["created_at"] = datetime.utcnow()
        result = await self.collection.insert_one(db_obj_in)
        assert result.acknowledged

        return await self.get(result.inserted_id)

    async def update(self, filter_obj: Dict, updated_obj: UpdateSchemaType):
        document = updated_obj.model_dump(by_alias=True, exclude_none=True)
        document["updated_at"] = datetime.utcnow()
        result = await self.collection.find_one_and_update(
            filter_obj, {"$set": document}, return_document=True
        )
        if not result:
            raise NotFoundException(identifier=str(filter_obj.get("_id")))
        return result

    async def delete(self, filter_obj: Dict):
        result = await self.collection.find_one_and_delete(filter_obj)
        if not result:
            raise NotFoundException(identifier=str(filter_obj.get("_id")))
        return result

    async def filter(
        self,
        filters: Dict[str, Any] = None,
        projection: List[str] = None,
        is_one: bool = True,
    ) -> Union[List[dict], List[Union[dict, Any]], Dict]:
        """Filter records based on given parameters and return selected fields from MongoDB."""

        projection_dict = {}

        if projection:
            projection_dict = {key: 1 for key in projection}

        cursor = self.collection.find(filters)
        results = [self.schema_model(**doc).model_dump() async for doc in cursor]
        if is_one:
            return results[0] if results else None

        return results
