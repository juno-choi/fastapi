from typing import Union
from fastapi import APIRouter

router2 = APIRouter()

@router2.get("/query/{id}")
async def path(id: str):
    return {
        "id" : id
    }

@router2.get("/query")
async def query(search: str, size: int = 10, page: Union[int, None] = None):
    # search - 필수값 / size - default=10 / page - null 가능
    return {
        "search" : search,
        "size" : size,
        "page" : page
    }