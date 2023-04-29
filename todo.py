from fastapi import APIRouter
from model import Todo

router = APIRouter()

todo_list  = []

@router.post("/todo")
async def add_todo(todo: Todo):
    todo_list.append(todo)

    return {
        "message" : "success"
    }

@router.get("/todo")
async def get_todo():
    return {
        "todo_list" : todo_list
    }