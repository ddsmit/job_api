from pydantic import BaseModel
from typing import Optional, List
from models.contact import Contact
import datetime

class Company(BaseModel):
    Name: str
    Desc: Optional[str]