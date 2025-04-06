from fastapi import APIRouter, Response, Request
from fastapi.responses import HTMLResponse, JSONResponse
from datetime import datetime, timedelta


general_router = APIRouter()

@general_router.get("/http")
def http(response: Response):
    response = HTMLResponse('<html><body><h1>Test</h1></body></html>')
    response.status_code = 500
    response.headers["appserver"] = "Server1"
    
    expiry = datetime.now() + timedelta(days=30)
    response.set_cookie("test", value="Value 1", expires=expiry.strftime("%a, %d %b %Y %H:%M:%S GMT")) # Cookie Expiry Date Format
    return response


@general_router.get("/cookie") # fly at user, whats wly looking inside Request
def http(response: Response, request: Request):
    v = request.cookies.get("test")
    return { "cookievalue": v }



@general_router.get("/")
async def home():
    return JSONResponse(content={"message": "Home page"})


@general_router.get("/about")
async def about():
    return JSONResponse(content={"message": "About page"})