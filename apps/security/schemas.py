
from pydantic import BaseModel


class UserCreate(BaseModel):
    password: str
    username: str


