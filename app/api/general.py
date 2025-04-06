from fastapi import APIRouter


general_router = APIRouter()

@general_router.get("/")
async def home():
    return {"message": "Home page"}


@general_router.get("/about")
async def about():
    return {"message": "About page"}