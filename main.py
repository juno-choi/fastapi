from fastapi import FastAPI
from todo import router

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(router)