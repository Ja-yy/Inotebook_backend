"""MODELS - USER
Models for user data including 'UserBase', 'UserCreate', and 'User' classes.
"""


from bson.objectid import ObjectId
from pydantic import BaseModel, EmailStr, Field

from app.models.common import DateTimeModelMixin


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
    Schema for representing a user with an additional 'id' field.
    """

    _id: ObjectId

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True


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

    email: EmailStr
    access_token: str
    token_type: str
