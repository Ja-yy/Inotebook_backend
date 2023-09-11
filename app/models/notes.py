"""MODELS - NOTES
Models for representing notes with title, description, tag, and creation timestamp.
"""

from typing import List, Optional

from pydantic import BaseModel, Field

from app.models.common import DateTimeModelMixin, PyObjectId


class NoteBase(DateTimeModelMixin):
    """
    Base schema for notes.
    """

    title: str = Field(..., description="Title of note")
    description: str = Field(..., description="Note context")
    tag: str = Field(description="Categorical tag", default="General")


class CreateNote(NoteBase):
    """
    Schema for creating notes.
    """

    user_id: Optional[PyObjectId] = Field(None)

    class Config:
        arbitrary_types_allowed = True


class Notes(NoteBase):
    """
    Schema for representing a note with an additional '_id' field.
    """

    note_id: PyObjectId = Field(..., alias="_id")

    class Config:
        arbitrary_types_allowed = True
        populate_by_name = True


class TagList(BaseModel):
    """
    Model for a list of tags.
    """

    tags: List[str]


class UpdateNote(BaseModel):
    """
    Schema for updating a note
    """

    title: str = Field(None, description="Title of note")
    description: str = Field(None, description="Note context")
    tag: str = Field(description="Categorical tag", default="General")
