from fastapi import APIRouter
from fastapi.responses import JSONResponse


general_router = APIRouter()


@general_router.get("/")
def home():
    return JSONResponse(content={ "message": f"Home page" })


@general_router.get("/about")
def about():
    return JSONResponse(content={ "message": "About page" })