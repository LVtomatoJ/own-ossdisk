from typing import Annotated
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from app.dependencies.db import DBSessionDep
from app.models.user import DBUser
from app.routers.schemas.common import TokenData
from app.routers.utils.user import get_one_user_by_username
from fastapi import Depends, HTTPException
from jose import JWTError, jwt

from app.config import settings

SECRET_KEY = settings.token_secret
ALGORITHM = "HS256"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
    session: DBSessionDep,
):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        print(payload)
        username: str = payload.get("username")
        if username is None:
            raise HTTPException(status_code=401, detail="username is None!")
        token_data = TokenData(username=username)
    except JWTError:
        raise HTTPException(status_code=401, detail="JWTError")
    user = get_one_user_by_username(session=session, username=token_data.username)
    if not user:
        raise HTTPException(status_code=401, detail="not user")
    return user


JWTAuthDep = Annotated[DBUser, Depends(get_current_user)]
