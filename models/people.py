from pydantic import BaseModel, EmailStr, HttpUrl
from typing import Optional

class Contact(BaseModel):
    id: Optional[str] = None
    Name: Optional[str] = None
    Phone: Optional[str] = None
    Email: Optional[EmailStr] = None
    LinkedIn: Optional[HttpUrl] = None

class User(BaseModel):
    Name: str
    Email: EmailStr
    LinkedIn: Optional[HttpUrl] = None
    Password: str