from pydantic import BaseModel, Field
from typing import Optional, List
from models.people import Contact
from models.company import Company
import datetime
import uuid


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
    id: str = Field(default_factory=uuid.uuid4, alias='_id')
    UserID: str
    Company: Company
    Title: str
    Statuses: Statuses
    Location: str
    PrimaryContact: Optional[Contact] = None
    Notes: Optional[str] = ""
    Salary: Optional[float] = ""
    Requirements: Optional[List[str]] = []

    class Config:
        allow_population_by_field_name = True


class JobUpdate(BaseModel):
    UserID: str
    Company: Company
    Title: str
    Statuses: Statuses
    Location: str
    PrimaryContact: Optional[Contact] = None
    Notes: Optional[str] = ""
    Salary: Optional[float] = ""
    Requirements: Optional[List[str]] = []
