from datetime import datetime, timedelta, timezone
from jose import jwt
from sqlmodel import select
from sqlmodel import Session

from app.models.user import DBUser
from app.config import settings

SECRET_KEY = settings.token_secret
ALGORITHM = "HS256"


def check_user_by_username_password(session: Session, username: str, password: str):
    statement = select(DBUser).where(
        DBUser.username == username, DBUser.password == password
    )
    results = session.exec(statement)
    user = results.first()
    return True if user else False


def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
