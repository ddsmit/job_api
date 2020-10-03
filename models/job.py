from pydantic import BaseModel
from typing import Optional, List
from models.people import Contact
from models.company import Company
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
    UserID: str
    Company: Company
    Title: str
    Statuses: Statuses
    Location: str
    PrimaryContact: Optional[Contact] = None
    Notes: Optional[str] = ""
    Salary: Optional[float] = ""
    Requirements: Optional[List[str]] = []
