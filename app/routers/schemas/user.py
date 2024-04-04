from pydantic import BaseModel
from sqlmodel import SQLModel


class UserRead(BaseModel):
    id: int
    username: str


class UserCreate(BaseModel):
    username: str
    password: str
