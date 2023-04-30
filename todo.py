from fastapi import APIRouter, HTTPException, status
from model import Todo, TodoItem, TodoItems

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

@router.get("/todo-items", response_model=TodoItems)
async def todo_items():
    return {
        "todos" : todo_list
    }

@router.get("/todo/{todo_id}")
async def get_todo(todo_id: int):
    for todo in todo_list:
        if todo.id == todo_id:
            return {
                "todo" : todo
            }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="not found todo id"
    )