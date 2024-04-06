from typing import Optional
from pydantic import BaseModel

from app.routers.schemas.common import UserRead


class FamilyCreate(BaseModel):
    name: str
    owner_user_id: Optional[int] = None


class FamilyRead(BaseModel):
    id: int
    name: str
    owner_user_id: int


class FamilyReadWithMembers(FamilyRead):
    members: list[UserRead] = []


class FamilyMemberSelect(BaseModel):
    user_id: Optional[int] = None
    username: Optional[int] = None
