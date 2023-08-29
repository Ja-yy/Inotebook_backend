from pydantic import BaseModel, EmailStr
from datetime import datetime


class User(BaseModel):
    """
    schema for Users
    """

    name: str
    email: EmailStr
    password: str
    created_at: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
