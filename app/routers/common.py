from datetime import timedelta
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status

from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from sqlmodel import Session

from app.database import get_session
from app.dependencies.db import DBSessionDep
from app.routers.utils.common import (
    check_user_by_username_password,
    create_access_token,
)

router = APIRouter()


class Token(BaseModel):
    access_token: str
    token_type: str


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.post("/token")
def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    session: DBSessionDep,
) -> Token:
    username = form_data.username
    password = form_data.password
    user = check_user_by_username_password(session, username, password)
    if not user:
        raise HTTPException(
            status_code=403, detail="登录失败，请检查用户名密码或用户状态"
        )
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(
        data={"username": username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")
