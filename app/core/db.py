import json
from fastapi import HTTPException
from sqlmodel import SQLModel, Session, create_engine, select
from models.ticket import TicketModel, Ticket

class JsonDatabase:

    _tickets = []
    _filename = "app/core/db.json"


    def load_database(self):
        with open(self._filename) as file:
            self._tickets = [TicketModel.model_validate(obj) for obj in json.load(file)]


    def save_database(self):
        with open(self._filename, 'w') as file:
            json.dump([ticket.model_dump() for ticket in self._tickets], file, indent=4) # type: ignore


    def get_tickets(self, status:str=None, title:str=None): # type: ignore
        tickets = self._tickets

        # we're can to go move by all json
        if status != None:
            tickets = [ticket for ticket in tickets if ticket.status.lower() == status.lower()]

        if title != None:
            tickets = [ticket for ticket in tickets if ticket.title == title]

        return tickets
    

    def get_one_ticket(self, id:int):
        try:
            _id = [ticket for ticket in self.get_tickets() if ticket.id == id]
            if _id:
                return _id[0]
            else:
                raise HTTPException(status_code=404, detail=f" {id} not found.")
        except KeyError as ke:
            raise HTTPException(status_code=500, detail=f" Key not found for {ke}")
        

    def append(self, item: TicketModel):
          # tools -- to apply `id`
        items = self.get_tickets()
        # обращаемся к последнему элементу и добавляем += 1
        # и проставляем дефолтное значение для колонки с `id`
        item.id = items[len(items) - 1].id + 1 # type: ignore # counter
        self._tickets.append(item)
        self.save_database()
    

    def delete(self, id:int):
        results = self.get_one_ticket(id)
        if results:
            self._tickets.remove(results) # type: ignore
            self.save_database()
            return results # type: ignore
        return results
    

class Database:
    _tickets = []
    def load_database(self):
        self.engine = create_engine(
            "sqlite:///ticket.db",
            connect_args={"check_same_thread": False}
        )
        SQLModel.metadata.create_all(self.engine)


    def save_database(self):
        ...

    def get_tickets(self, status:str=None, title:str=None): # type: ignore
        with Session(self.engine) as session:
            query = select(Ticket)

            if status != None:
                query = query.where(Ticket.status == status)

            if title != None:
                query = query.where(Ticket.title == title)

            return session.exec(query).all()
    

    def get_one_ticket(self, id:int):
        try:
            _id = [ticket for ticket in self.get_tickets() if ticket.id == id]
            if _id:
                return _id[0]
            else:
                raise HTTPException(status_code=404, detail=f" {id} not found.")
        except KeyError as ke:
            raise HTTPException(status_code=500, detail=f" Key not found for {ke}")


    def append(self, item: TicketModel):
        with Session(self.engine) as session:
            ticket = Ticket.model_validate(item) # type: ignore
            session.add(ticket)
            session.commit()
            session.refresh(ticket)
        return ticket
    

    def delete(self, id:int):
        results = self.get_one_ticket(id)
        if results:
            self._tickets.remove(results) # type: ignore
            self.save_database()
            return results # type: ignore
        return results