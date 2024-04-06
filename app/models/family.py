from typing import TYPE_CHECKING
from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from app.models.user import DBUser


class DBFamily(SQLModel, table=True):
    __tablename__ = "family"

    id: int | None = Field(default=None, primary_key=True)
    name: str
    owner_user_id: int = Field(unique=True)
    members: list["DBUser"] = Relationship(back_populates="family")
