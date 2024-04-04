from pydantic import ConfigDict
from sqlmodel import SQLModel, Field


class DBUser(SQLModel, table=True):

    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(unique=True)
    password: str
