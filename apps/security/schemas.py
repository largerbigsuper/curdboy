
from pydantic import BaseModel


class UserPassword(BaseModel):
    password: str

class UserCreate(BaseModel):
    password: str
    username: str


class UserPasswordChange(BaseModel):
    password: str
    new_password: str


class UserPasswordReset(BaseModel):
    password: str
    username: str
    code: str


