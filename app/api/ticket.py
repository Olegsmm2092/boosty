from typing import List
from fastapi import HTTPException, APIRouter
from core import Database, JsonDatabase
from models.ticket import TicketModel, Ticket


db = Database()
db.load_database()

ticket_router = APIRouter(prefix='/ticket')


@ticket_router.get("/", response_model=List[TicketModel])
def tickets(status:str=None, title:str=None): # type: ignore
    return db.get_tickets(status, title) # type: ignore
   

@ticket_router.get("//{id}", response_model=TicketModel)
def ticket(id:int):
    return db.get_one_ticket(id)


@ticket_router.put("/", response_model=Ticket)
def ticketput(item:TicketModel):
    return db.append(item)


@ticket_router.patch("/", response_model=TicketModel)
def ticketpatch(item:TicketModel): # inside model has id can usage them
    # whats to do
    result = db.update(item) # type: ignore
    if result:
        return result
    else:
        raise HTTPException(status_code=404, detail=f"{item.id} not found")


@ticket_router.delete("/{id}")
def ticketdel(id:int): # type: ignore
    return db.delete(id)
