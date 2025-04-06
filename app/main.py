from fastapi import FastAPI
from api.ticket import ticket_router
from api.general import general_router
import uvicorn


app = FastAPI(title="Service of Tickets")
app.include_router(ticket_router, prefix='/api')
app.include_router(general_router, prefix='/api')



if __name__ == '__main__':
    uvicorn.run("main:app", port=8080, reload=True) # yb said by terminal best choice