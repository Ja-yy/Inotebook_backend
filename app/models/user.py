"""MODELS - USER
Models for user data including 'UserBase', 'UserCreate', and 'User' classes.
"""


from pydantic import BaseModel, EmailStr, Field

from app.models.common import DateTimeModelMixin, PyObjectId


class UserCreate(DateTimeModelMixin):
    """
    Schema for creating a user.
    """

    name: str = Field(..., description="User name")
    email: EmailStr = Field(..., description="User email address")
    password: str = Field(..., description="User Password")


class User(UserCreate):
    """
    Schema for representing a user with an additional '_id' field.
    """

    user_id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_schema_extra = {
            "example": {
                "name": "Jane Doe",
                "email": "jdoe@example.com",
                "password": "$jlsajdlsajdlj4385943v4nv",
            }
        }


class SignUpRes(BaseModel):
    """
    Response model for signup.
    """

    name: str = Field(..., description="User name")
    email: EmailStr = Field(..., description="User email address")


class UserSignin(BaseModel):
    """
    Schema for user signin
    """

    email: EmailStr = Field(..., description="User email address")
    password: str = Field(..., description="User Password")


class UserSigninRes(BaseModel):
    """
    Response model for user signin.
    """

    email: EmailStr = Field(..., description="User email address")
    user_id: PyObjectId = Field(...)
    access_token: str = Field(...)
    token_type: str = Field(...)

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
