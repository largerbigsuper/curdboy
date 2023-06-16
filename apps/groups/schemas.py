
from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class GroupCreate(BaseModel):
    name: str
    sort: int
    avatar: Optional[str]
    is_active: bool

class GroupUpdate(BaseModel):
    name: str
    sort: int
    avatar: Optional[str]
    is_active: bool

class Group(BaseModel):
    id: int
    name: str
    sort: int
    avatar: Optional[str]
    is_active: bool
    created_time: datetime
    updated_time =datetime

    class Config:
        orm_mode = True