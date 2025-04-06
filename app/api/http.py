from ast import For
from fastapi import APIRouter, Response, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from datetime import datetime, timedelta

from typing import Annotated


http_router = APIRouter()

@http_router.get("/http")
def http(response: Response):
    response = HTMLResponse('<html><body><h1>Test</h1></body></html>')
    response.status_code = 500
    response.headers["appserver"] = "Server1"
    
    expiry = datetime.now() + timedelta(days=30)
    response.set_cookie("test",
                        value="Value 1",
                        expires=expiry.strftime("%a, %d %b %Y %H:%M:%S GMT"),
                        httponly=True
                           
    ) # Cookie Expiry Date Format
    return response


@http_router.get("/cookie") # fly at user, whats wly looking inside Request
def cookie(response: Response, request: Request):
    v = request.cookies.get("test")
    return { "cookievalue": v }


@http_router.get("/request")
def request(request: Request):
    v = request.query_params.get("a")
    return { "paramvalue": v }




@http_router.post("/form")
def request(
    request: Request,
    username: Annotated[str, Form()],
    data: Annotated[str | None, Form()]=None):
    return { "username": username, "data": data }


@http_router.post("/mform")
async def request(request: Request):
    f = await request.form()
    username = f.get("username")
    data = f.get("data")
    return { "username 1": username, "data 1": data }
