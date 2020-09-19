from pydantic import BaseModel
from typing import Optional, List
from models.contact import Contact
import datetime

class Status(BaseModel):
    Completed: bool = False
    Date: Optional[datetime.datetime] = None

class Statuses(BaseModel):
    Applied: Status
    PhoneScreen: Status
    Interview: Status
    Offer: Status
    Rejected: Status

class Job(BaseModel):
    Company: str
    Title: str
    Statuses: Statuses
    Location: str
    PrimaryContact: Optional[Contact] = None
    Notes: Optional[str] = ""
    Salary: Optional[float] = ""
    Requirements: Optional[List[str]] = []
