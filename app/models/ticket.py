from pydantic import BaseModel


class TicketModel(BaseModel):
    id: int
    title: str|None = None
    status: str = "Draft"
    type: str = "Bug"

