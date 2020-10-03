from pydantic import BaseModel
from typing import Optional, List
from models.people import Contact
import datetime

class Company(BaseModel):
    id: Optional[str] = None
    Name: Optional[str] = None
    Desc: Optional[str] = None