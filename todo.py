from fastapi import APIRouter, HTTPException, Path, status, Request, Depends
from fastapi.templating import Jinja2Templates
from model import Todo, TodoItem, TodoItems

router = APIRouter()

todo_list  = []

template = Jinja2Templates(directory="templates/")

@router.post("/todo")
async def add_todo(request: Request, todo: Todo = Depends(Todo.as_form)):
    todo.id = len(todo_list) +1
    todo_list.append(todo)

    return template.TemplateResponse("todo.html", 
        {
            "request" : request,
            "todos" : todo_list
        }
    )

@router.get("/todo")
async def get_todo(request: Request):
    return template.TemplateResponse("todo.html",
        {
            "request": request,
            "todos" : todo_list
        }
    )


@router.get("/todo/{todo_id}")
async def get_todo_single(request: Request, todo_id: int = Path(..., title="The ID of the todo to retrive.")):
    for todo in todo_list:
        if todo.id == todo_id:
            return template.TemplateResponse("todo.html",
                {
                    "request" : request,
                    "todo" : todo
                }
            )
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="not found todo id"
    )

@router.get("/todo-items", response_model=TodoItems)
async def todo_items():
    return {
        "todos" : todo_list
    }
