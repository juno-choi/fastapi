from fastapi import FastAPI
from todo import router
from get import router2

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(router)
app.include_router(router2)