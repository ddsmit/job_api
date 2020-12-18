from pydantic import BaseModel, EmailStr, HttpUrl, Field
from typing import Optional
import uuid

class Contact(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias='_id')
    Name: Optional[str] = None
    Phone: Optional[str] = None
    Email: Optional[EmailStr] = None
    LinkedIn: Optional[HttpUrl] = None

    class Config:
        allow_population_by_field_name = True


class User(BaseModel):
    Name: str
    Email: EmailStr
    LinkedIn: Optional[HttpUrl] = None
    Password: str