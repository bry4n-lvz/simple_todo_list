from pydantic import BaseModel
from datetime import datetime

class Task(BaseModel):
    name: str
    description: str
    due_date: datetime
    checkbox: bool = False