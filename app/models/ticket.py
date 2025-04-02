from enum import Enum
from pydantic import BaseModel, Field, validator
import re

class BugType(str, Enum):
    Bug = 'Bug'
    Story = 'Story'
    Epic = 'Epic'

class StatusType(str, Enum):
    Draft = 'Draft'
    Published = 'Published'
    InProgress = 'In progress'

class TicketModel(BaseModel):
    id: int
    title: str|None = Field(max_length=30, default=None, alias='Title')
    status: StatusType = StatusType.Draft
    type: BugType = BugType.Bug
    severity: int = Field(default=0, ge=0, lt=10)



