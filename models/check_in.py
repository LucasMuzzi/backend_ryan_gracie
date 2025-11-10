from beanie import Document
from datetime import date, datetime, time
from uuid import uuid4
from pydantic import Field


class CheckIn(Document):
    id: str = Field(default_factory=lambda: str(uuid4()))
    client_name: str
    checkin_datetime: datetime
    created_at: datetime = Field(default_factory=datetime.now)
