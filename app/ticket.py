from typing import List
from fastapi import FastAPI, HTTPException
import uvicorn
from core.db import Database, JsonDatabase
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


@app.get("/tickets/", response_model=List[TicketModel])
def tickets(status:str=None, title:str=None): # type: ignore
    return db.get_tickets(status, title) # type: ignore
   

@app.get("/tickets/{id}", response_model=TicketModel)
def ticket(id:int):
    return db.get_one_ticket(id)

@app.put("/ticket", response_model=Ticket)
def ticketput(item:TicketModel):
    return db.append(item)

@app.patch("/ticket", response_model=TicketModel)
def ticketpatch(item:TicketModel): # inside model has id can usage them
    # whats to do
    result = db.update(item) # type: ignore
    if result:
        return result
    else:
        raise HTTPException(status_code=404, detail=f"{item.id} not found")

@app.delete("/ticket/{id}")
def ticketdel(id:int): # type: ignore
    return db.delete(id)


if __name__ == '__main__':
    uvicorn.run("ticket:app", port=8080, reload=True) # yb said by terminal best choice