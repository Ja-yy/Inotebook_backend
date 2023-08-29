from pydantic import BaseModel
from datetime import datetime


class Notes(BaseModel):
    """
    schems for Notes
    """

    title: str
    description: str
    tag: str | None = "General"
    created_at: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
