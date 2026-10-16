from typing import List, Optional
from pydantic import BaseModel, Field
from fastapi import Form
class Todo(BaseModel):
    id: Optional[int] = None
    item: str = Field(..., min_length=1)

    @classmethod
    def as_form(cls, item: str = Form(..., min_length=1)):
        return cls(item=item)



class TodoItem(BaseModel):
    item: str

    class Config:
        json_schema_extra = {
            "example": {
                "item": "Read the next chapter of the book."
            }
        }


class TodoItems(BaseModel):
    todos: List[TodoItem]

    class Config:
        json_schema_extra = {
            "example": {
                "todos": [
                    {"item": "Example schema 1!"},
                    {"item": "Example schema 2!"},
                ]
            }
        }
