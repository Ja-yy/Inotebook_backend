"""MODELS - NOTES
Models for representing notes with title, description, tag, and creation timestamp.
"""

from datetime import datetime

from pydantic import BaseModel


class Notes(BaseModel):
    """
    Notes schema.
    """

    title: str
    description: str
    tag: str | None = "General"
    created_at: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
