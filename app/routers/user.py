from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlmodel import Session

from app.database import get_session
from app.dependencies.db import DBSessionDep
from app.models.user import DBUser
from app.routers.schemas.user import UserCreate, UserRead
from app.dependencies.auth import get_current_user
from app.routers.utils.user import create_one_user, get_one_user_by_username


router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.get("/users/", response_model=UserRead)
def read_users(
    current_user: Annotated[DBUser, Depends(get_current_user)],
):
    return current_user


@router.post("/user/", response_model=UserRead)
def create_user(user: UserCreate, session: Session = Depends(get_session)):
    is_exist = get_one_user_by_username(session=session, username=user.username)
    if is_exist:
        raise HTTPException(status_code=400, detail="Username exist!")
    user = create_one_user(session=session, user=user)
    return user
