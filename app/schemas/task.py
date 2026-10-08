from pydantic import BaseModel, Field
from typing import Optional


class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    description: Optional[str] = Field(None, max_length=1000)
    done: bool = False


class TaskUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=200)
    description: Optional[str] = Field(None, max_length=1000)
    done: Optional[bool] = None


class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    done: bool

    model_config = {"from_attributes": True}