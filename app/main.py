from fastapi import FastAPI
from api import ticket_router, general_router, http_router
import uvicorn


app = FastAPI(title="Service of Tickets")
app.include_router(ticket_router, prefix='/api')
app.include_router(general_router, prefix='/api')
app.include_router(http_router, prefix='/api')



if __name__ == '__main__':
    uvicorn.run("main:app", port=8080, reload=True) # yb said by terminal best choice