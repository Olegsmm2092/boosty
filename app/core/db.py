import json
from fastapi import HTTPException
from models.ticket import TicketModel

class Database:

    _tickets = []
    _filename = "app/core/db.json"

    def load_database(self):
        with open(self._filename) as file:
            self._tickets = [TicketModel.model_validate(obj) for obj in json.load(file)]

    def save_database(self):
        with open(self._filename, 'w') as file:
            json.dump([ticket.model_dump() for ticket in self._tickets], file, indent=4) # type: ignore

    def get_tickets(self):
        return self._tickets
    
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
        self._tickets.append(item)
        self.save_database()
    
    def delete(self, id:int):
        results = self.get_one_ticket(id)
        if results:
            self._tickets.remove(results) # type: ignore
            self.save_database()
            return results # type: ignore
        return results