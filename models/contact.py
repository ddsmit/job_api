from pydantic import BaseModel, EmailStr, HttpUrl
from typing import Optional

class Contact(BaseModel):
    Name: Optional[str]
    Phone: Optional[str]
    Email: Optional[EmailStr]
    LinkedIn: HttpUrl