from typing import List, Optional
from fastapi import Form
from pydantic import BaseModel

class Todo(BaseModel):
    id: Optional[int]
    item: str

    @classmethod
    def as_form(
        cls,
        item: str = Form(...)
    ):
        return cls(item=item)

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