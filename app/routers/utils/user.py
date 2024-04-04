from sqlmodel import select
from sqlmodel import Session

from app.models.user import DBUser
from app.routers.schemas.user import UserCreate


def get_one_user_by_username(session: Session, username: str):
    results = session.exec(select(DBUser).where(DBUser.username == username))
    user = results.first()
    return user


def create_one_user(session: Session, user: UserCreate):
    user_model: DBUser = DBUser.model_validate(user)
    session.add(user_model)
    session.commit()
    session.refresh(user_model)
    return user_model
