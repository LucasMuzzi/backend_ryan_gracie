from datetime import datetime
from uuid import uuid4
from beanie import Document
from pydantic import EmailStr, Field


class Personal(Document):
    id: str = Field(default_factory=lambda: str(uuid4()))
    full_name: str
    email: EmailStr
    password: str
    created_at: datetime = Field(default_factory=datetime.now)


class PersonalClients(Document):
    id: str = Field(default_factory=lambda: str(uuid4()))
    personal_id: str
    full_name: str
    email: EmailStr
    born_date: datetime
    gender: str
    color_belt: str
    contact_number: str
    active: bool = False
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
