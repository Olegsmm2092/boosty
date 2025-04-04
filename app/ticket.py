from typing import List
from fastapi import FastAPI
import uvicorn
from core.db import Database
from models.ticket import TicketModel, Ticket


# import setting of project via config.py.
# from app.core.config import settings


# app = FastAPI(title=settings.app_title)
app = FastAPI(title="Service of Tickets")
# локально у нас уже база данных подгужена
# это самое большое выделение памяти
db = Database()
db.load_database()

@app.get("/")
async def home():
    return {"message": "Home page"}


@app.get("/about")
async def about():
    return {"message": "About page"}


@app.get("/tickets", response_model=List[TicketModel])
def tickets(status:str=None, title:str=None): # type: ignore
    return db.get_tickets(status, title) # type: ignore
   

@app.get("/tickets/{id}", response_model=TicketModel)
def ticket(id:int):
    return db.get_one_ticket(id)

@app.put("/ticket", response_model=Ticket)
def ticketput(item:TicketModel):
    return db.append(item)

@app.patch("/ticket")
def ticketpatch(item:TicketModel): # inside model has id can usage them
    # whats to do
    results = [ticket for ticket in db.get_tickets() if ticket.id == item.id] # fetchone
    if results:
        results[0].title = item.title
        results[0].status = item.status
        results[0].type = item.type
        # whats to do after apply modification
        db.save_database()
    return item

@app.delete("/ticket/{id}")
def ticketdel(id:int): # type: ignore
    return db.delete(id)


if __name__ == '__main__':
    uvicorn.run("ticket:app", port=8080, reload=True) # yb said by terminal best choice