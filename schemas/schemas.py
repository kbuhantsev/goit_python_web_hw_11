from typing import Optional

from pydantic import BaseModel, Field, EmailStr, HttpUrl


class User(BaseModel):
    name: str
    email: EmailStr
    website: HttpUrl
    age: Optional[int] = Field(default=89, ge=13, le=90)
    friends: Optional[int] = 0


user = User(name="John", email="john@example.com", website="https://john.com", friends=10)
print(user)
