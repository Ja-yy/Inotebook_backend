"""MODEL - COMMON
Common models to inherit
"""

from datetime import datetime
from typing import Annotated, Optional, Union

from bson.objectid import ObjectId
from pydantic import BaseModel, Field
from pydantic.functional_validators import AfterValidator


class DateTimeModelMixin(BaseModel):
    """
    DateTimeModelMixin is a base model class that provides timestamp fields.
    """

    created_at: Optional[datetime] = Field(None)
    updated_at: Optional[datetime] = Field(None)


PyObjectId = Annotated[
    Union[ObjectId, str],
    AfterValidator(lambda x: str(x) if ObjectId.is_valid else None),
    AfterValidator(str),
]


"""
`PyObjectId` is a type alias representing a value that can be either an `ObjectId` or a string.

Usage:
- It allows flexibility in accepting either an `ObjectId` or a string as an identifier.
- If an `ObjectId` is provided, it is converted to a string representation.
- If the provided value is not a valid `ObjectId`, it returns `None`.

Example:
    - Valid `ObjectId`: `ObjectId('60c7b5c2d480f3a7f94c1d90')`
    - Corresponding `PyObjectId`: `'60c7b5c2d480f3a7f94c1d90'`
    - Invalid value: `'invalid_id'`
    - Corresponding `PyObjectId`: `None`
"""
