import json
from fastapi import HTTPException
from models.ticket import TicketModel


class JsonDatabase:

    _tickets = []
    _filename = "app/db/db.json"


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
    

    def get_ticket(self, id:int):
        results = [ticket for ticket in self.get_tickets() if ticket.id == id]
        if results:
            return results[0]
        return None


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
        return item
    

    def update(self, item: TicketModel):
        results = [ticket for ticket in self.get_tickets() if ticket.id == item.id] # type: ignore # fetchone
        if results:
            # whats to do after apply modification
            results[0].title = item.title
            results[0].status = item.status
            results[0].type = item.type
            results[0].severity = item.severity
            self.save_database()
        return item


    def delete(self, id:int):
        results = self.get_one_ticket(id)
        if results:
            self._tickets.remove(results) # type: ignore
            self.save_database()
            return results # type: ignore
        return results
    