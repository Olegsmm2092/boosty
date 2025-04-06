from fastapi import HTTPException
from sqlmodel import SQLModel, Session, create_engine, select
from models.ticket import TicketModel, Ticket



class Database:
    def load_database(self):
        self.engine = create_engine(
            "sqlite:///app/db/ticket.db",
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
    
    
    def get_ticket(self, id:int):
        with Session(self.engine) as session:
            return session.get(Ticket, id)


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
    

    def update(self, item: TicketModel):
        with Session(self.engine) as session:
            ticket = session.get(Ticket, item.id)
            if ticket:
                ticket.title = item.title
                ticket.status = item.status
                ticket.type = item.type
                ticket.severity = item.severity
                session.commit()
                return ticket


    def delete(self, id:int):
        with Session(self.engine) as session:
            ticket = session.get(Ticket, id)
            if ticket:
                session.delete(ticket)
                session.commit()
                return ticket
        return None