from datetime import datetime
from pydantic import BaseModel


class CheckInSchema(BaseModel):
    client_name: str
    checkin_date: datetime
