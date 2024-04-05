from pydantic import BaseModel

from app.routers.schemas.common import UserRead
from app.routers.schemas.family import FamilyRead


class UserReadWithFamily(UserRead):
    family: FamilyRead | None = None


class UserCreate(BaseModel):
    username: str
    password: str
