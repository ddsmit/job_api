from pydantic import BaseModel, Field
from typing import Optional
import uuid

class Company(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias='_id')
    Name: Optional[str] = None
    Desc: Optional[str] = None

    class Config:
        allow_population_by_field_name = True