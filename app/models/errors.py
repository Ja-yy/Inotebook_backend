"""MODELS - ERRORS
Models for Error responses. Custom exceptions must be associated with one of these
"""

# # Installed # #
from pydantic import BaseModel, Field

__all__ = (
    "BaseError",
    "BaseIdentifiedError",
    "NotFoundError",
    "AlreadyExistsError",
    "WrongCredentialsError",
)


class BaseError(BaseModel):
    message: str = Field(..., description="Error message or description")


class BaseIdentifiedError(BaseError):
    identifier: str = Field(
        ..., description="Unique identifier which this error references to"
    )


class NotFoundError(BaseIdentifiedError):
    """The entity does not exist"""


class AlreadyExistsError(BaseIdentifiedError):
    """An entity being created already exists"""


class WrongCredentialsError(BaseIdentifiedError):
    """Wrong Credential provided"""
