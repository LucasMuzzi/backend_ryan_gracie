from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, Field


class PersonalCreateSchema(BaseModel):
    full_name: str
    email: EmailStr
    password: str


class PersonalClientSchema(BaseModel):
    personal_id: str
    full_name: str
    email: EmailStr
    born_date: datetime
    gender: str
    color_belt: str
    contact_number: str
    active: Optional[bool] = False
    created_at: Optional[datetime] = Field(default_factory=datetime.now)
    updated_at: Optional[datetime] = Field(default_factory=datetime.now)
