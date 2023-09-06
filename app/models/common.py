"""MODEL - COMMON
Common models to inherit
"""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class DateTimeModelMixin(BaseModel):
    created_at: Optional[datetime] = Field(None)
    updated_at: Optional[datetime] = Field(None)
