from datetime import date
from typing import Optional

from pydantic import BaseModel, Field, EmailStr, HttpUrl


class ContactModel(BaseModel):
    name: str = Field(min_length=3, max_length=50)
    surname: str = Field(min_length=3, max_length=50)
    email: EmailStr = Field(default=None)
    phone: Optional[str] = Field(default=None)
    date_of_birth: Optional[date] = Field(default=None)

