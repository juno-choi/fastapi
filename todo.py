from fastapi import APIRouter

router = APIRouter()

@router.get("/hello")
async def hello():
    return {
        "message" : "hello"
    }

@router.get("/hello2")
async def hello2():
    return {
        "message":"hello2"
    }