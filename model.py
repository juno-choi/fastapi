from typing import List
from pydantic import BaseModel

class Todo(BaseModel):
    id: int
    item: str
    class Config:
        schema_extra = {
            "example" : {
                "id" : 100,
                "item" : "밥먹기"
            }
        }

class TodoItem(BaseModel):
    item: str
    class Config:
        schema_extra = {
            "example" : {
                "item" : "Read the next chapter of the book"
            }
        }

class TodoItems(BaseModel):
    todos: List[TodoItem]
    class Config:
        schema_extra = {
            "example": {
                "todos" : [
                    {
                        "id" : 1,
                        "item" : "1"
                    },
                    {
                        "id": 2,
                        "item" : "2"
                    }
                ]
            }
        }