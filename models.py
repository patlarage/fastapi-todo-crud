from pydantic import BaseModel, Field
from typing import Optional

class Todo(BaseModel):
    id:int
    title: str= Field(..., min_length=1,max_length=100)
    description: Optional[str]=""
    completed: bool=False
    
    
class TodoCreate(BaseModel):
    title: str=Field(..., min_length=1, max_length=100)
    description: Optional[str] = ""