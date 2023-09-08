"""MODEL - COMMON
Common models to inherit
"""

from datetime import datetime
from typing import Any, Callable, Dict, Optional

from bson.objectid import ObjectId
from pydantic import BaseModel, Field, GetJsonSchemaHandler
from pydantic_core import CoreSchema, core_schema


class DateTimeModelMixin(BaseModel):
    created_at: Optional[datetime] = Field(None)
    updated_at: Optional[datetime] = Field(None)


class CustomObjectId(ObjectId):
    @classmethod
    def __get_pydantic_core_schema__(
        cls, source: type[Any], handler: Callable[[Any], core_schema.CoreSchema]
    ) -> core_schema.CoreSchema:
        return core_schema.general_plain_validator_function(function=cls.validate)

    @classmethod
    def validate(cls, v, *kargs):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return str(v)

    @classmethod
    def __get_pydantic_json_schema__(
        cls, core_schema: CoreSchema, handler: GetJsonSchemaHandler
    ) -> Dict[str, Any]:
        json_schema = handler(core_schema)
        json_schema.update(type="string")
        return json_schema
