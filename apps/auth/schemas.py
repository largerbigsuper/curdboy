
from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class UserCreate(BaseModel):
    password: str
    username: str


class UserUpdate(BaseModel):
    nickname: Optional[str]
    gender: Optional[str]
    avatar: Optional[str]
    email: Optional[str]
    is_superuser: bool
    is_active: bool

class User(BaseModel):
    id: int
    username: str
    nickname: Optional[str]
    gender: Optional[str]
    avatar: Optional[str]
    email: Optional[str]
    password: Optional[str]
    is_superuser: bool
    is_active: bool
    created_time: datetime
    updated_time =datetime
    last_login = datetime

    class Config:
        orm_mode = True

## Groups

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