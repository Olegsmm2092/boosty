from typing import List
from fastapi import HTTPException, APIRouter
from core.db import Database, JsonDatabase
from models.ticket import TicketModel, Ticket


db = Database()
db.load_database()

ticket_router = APIRouter()

@ticket_router.get("/")
async def home():
    return {"message": "Home page"}


@ticket_router.get("/about")
async def about():
    return {"message": "About page"}


@ticket_router.get("/tickets/", response_model=List[TicketModel])
def tickets(status:str=None, title:str=None): # type: ignore
    return db.get_tickets(status, title) # type: ignore
   

@ticket_router.get("/tickets/{id}", response_model=TicketModel)
def ticket(id:int):
    return db.get_one_ticket(id)

@ticket_router.put("/ticket", response_model=Ticket)
def ticketput(item:TicketModel):
    return db.append(item)

@ticket_router.patch("/ticket", response_model=TicketModel)
def ticketpatch(item:TicketModel): # inside model has id can usage them
    # whats to do
    result = db.update(item) # type: ignore
    if result:
        return result
    else:
        raise HTTPException(status_code=404, detail=f"{item.id} not found")

@ticket_router.delete("/ticket/{id}")
def ticketdel(id:int): # type: ignore
    return db.delete(id)
