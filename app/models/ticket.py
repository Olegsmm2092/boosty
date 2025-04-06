from sqlalchemy import table
from sqlmodel import SQLModel, Field
from enum import Enum


class BugType(str, Enum):
    Bug = 'Bug'
    Story = 'Story'
    Epic = 'Epic'

class StatusType(str, Enum):
    Draft = 'Draft'
    Published = 'Published'
    InProgress = 'In progress'

class TicketModel(SQLModel):
    id: int|None = None
    title: str|None = Field(max_length=30, default=None, alias='Title')
    status: StatusType = StatusType.Draft
    type: BugType = BugType.Bug
    severity: int = Field(default=0, ge=0, lt=10)

class Ticket(TicketModel, table=True):
    id: int|None = Field(primary_key=True, default=None)

