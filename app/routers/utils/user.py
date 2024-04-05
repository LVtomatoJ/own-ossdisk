from sqlmodel import select
from sqlmodel import Session

from app.models.family import DBFamily
from app.models.oss import DBOss
from app.models.user import DBUser
from app.routers.schemas.family import FamilyCreate
from app.routers.schemas.oss import OssAccountCreate
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


def create_one_oss_account(
    session: Session, oss_account: OssAccountCreate, user_id: int
):
    oss_account.user_id = user_id
    oss_account_model: DBOss = DBOss.model_validate(oss_account)
    session.add(oss_account_model)
    session.commit()
    session.refresh(oss_account_model)
    return oss_account_model


def delete_one_oss_account(session: Session, oss_account: DBOss):
    session.delete(oss_account)
    session.commit()


def get_one_oss_account_by_id(session: Session, oss_account_id: int):
    results = session.exec(select(DBOss).where(DBOss.id == oss_account_id))
    oss_account_model: DBOss = results.first()
    return oss_account_model


def get_user_oss_accounts_by_user_id(session: Session, user_id: int):
    pass


def create_one_family(session: Session, family: FamilyCreate):
    family_model: DBFamily = DBFamily.model_validate(family)
    session.add(family_model)
    session.commit()
    session.refresh(family_model)
    return family_model
