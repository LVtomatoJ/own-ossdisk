from typing import TYPE_CHECKING, Optional
from sqlmodel import Relationship, SQLModel, Field

from app.models.family import DBFamily


if TYPE_CHECKING:

    from app.models.oss import DBOss


class DBUser(SQLModel, table=True):

    __tablename__ = "user"

    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(unique=True)
    password: str
    oss_accounts: list["DBOss"] = Relationship(back_populates="user")
    family_id: int | None = Field(default=None, foreign_key="family.id")
    family: Optional["DBFamily"] | None = Relationship(back_populates="members")
