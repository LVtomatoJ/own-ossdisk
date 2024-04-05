from enum import Enum
from typing import TYPE_CHECKING, Optional
from sqlmodel import Relationship, SQLModel, Field

from app.routers.schemas.oss import PlateFormEnum

from app.models.user import DBUser


class DBOss(SQLModel, table=True):

    __tablename__ = "oss_account"

    id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    user: DBUser = Relationship(back_populates="oss_accounts")
    ak: str
    sk: str
    plateform: PlateFormEnum
