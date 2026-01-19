from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime


class Task(SQLModel, table=True):
    """Task stored in database."""
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(min_length=1, max_length=200)
    description: Optional[str] = None
    status: str = Field(default="pending")
    created_at: datetime = Field(default_factory=datetime.utcnow)