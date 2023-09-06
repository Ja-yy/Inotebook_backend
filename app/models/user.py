"""MODELS - USER
Models for user data including 'UserBase', 'UserCreate', and 'User' classes.
"""


from typing import Optional

from bson.objectid import ObjectId
from pydantic import BaseModel, EmailStr, Field

from app.models.common import DateTimeModelMixin, PyObjectId


class UserBase(DateTimeModelMixin):
    """
    Base schema for user.
    """

    name: str = Field(..., description="User name")
    email: EmailStr = Field(..., description="User email address")
    password: str = Field(..., description="User Password")


class UserCreate(UserBase):
    """Schema for creating a user."""


class User(UserBase):
    """
    Schema for representing a user with an additional '_id' field.
    """

    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class SignUpResponse(BaseModel):
    """response model for sigup"""

    name: str = Field(..., description="User name")
    email: EmailStr = Field(..., description="User email address")


class UserSignin(BaseModel):
    """Schema foe signin"""

    email: EmailStr = Field(..., description="User email address")
    password: str = Field(..., description="User Password")


class UserSigninResponse(BaseModel):
    """Response model for signin"""

    id: Optional[PyObjectId]
    email: EmailStr
    access_token: str
    token_type: str

    class Config:
        arbitrary_types_allowed = True
