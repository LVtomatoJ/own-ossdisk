from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlmodel import Session, select

from app.database import get_session
from app.dependencies.db import DBSessionDep
from app.models.family import DBFamily
from app.models.user import DBUser
from app.routers.schemas.family import (
    FamilyCreate,
    FamilyMemberSelect,
    FamilyReadWithMembers,
)
from app.routers.schemas.oss import OssAccountCreate, OssAccountRead
from app.routers.schemas.user import UserCreate, UserRead, UserReadWithFamily
from app.dependencies.auth import get_current_user
from app.routers.utils.user import (
    create_one_family,
    create_one_oss_account,
    create_one_user,
    delete_one_oss_account,
    get_one_oss_account_by_id,
    get_one_user_by_username,
    get_user_oss_accounts_by_user_id,
)


router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.get("/users/", response_model=UserReadWithFamily)
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


@router.post("/user/oss-account")
def create_oss_account(
    oss_account: OssAccountCreate,
    current_user: Annotated[DBUser, Depends(get_current_user)],
    session: Session = Depends(get_session),
):
    oss_account = create_one_oss_account(
        session=session, oss_account=oss_account, user_id=current_user.id
    )
    return oss_account


@router.delete("/user/oss-account/{oss_account_id}")
def delete_oss_account(
    oss_account_id: int,
    current_user: Annotated[DBUser, Depends(get_current_user)],
    session: Session = Depends(get_session),
):
    # 检查是否存在&&是否是自己的
    oss_account = get_one_oss_account_by_id(
        session=session, oss_account_id=oss_account_id
    )
    if not oss_account:
        raise HTTPException(status_code=404, detail="oss_account not found")
    if oss_account.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="not your oss_account")
    delete_one_oss_account(session=session, oss_account=oss_account)
    return {"msg": "success"}


@router.get("/user/oss-accounts")
def get_user_oss_accounts(
    current_user: Annotated[DBUser, Depends(get_current_user)],
    session: Session = Depends(get_session),
) -> list[OssAccountRead]:
    """
    获取用户所有oss账号
    """
    user_oss_accounts = current_user.oss_accounts
    return user_oss_accounts


@router.post("/user/famliy")
def create_user_famliy(
    family: FamilyCreate,
    current_user: Annotated[DBUser, Depends(get_current_user)],
    session: Session = Depends(get_session),
) -> FamilyReadWithMembers:
    """
    创建用户家庭
    """
    if not family.owner_user_id:
        family.owner_user_id = current_user.id
    else:
        if family.owner_user_id != current_user.id:
            raise HTTPException(
                status_code=403,
                detail="family owner_user_id must be current_user.id",
            )
    family_in_db = create_one_family(session, family)
    current_user.family = family_in_db
    session.commit()
    return family_in_db


@router.get("/user/family")
def get_my_family(
    current_user: Annotated[DBUser, Depends(get_current_user)],
    session: Session = Depends(get_session),
) -> FamilyReadWithMembers:
    """
    获取用户家庭
    """
    family = current_user.family
    return family


@router.post("/user/family/memeber")
def add_member_to_family(
    current_user: Annotated[DBUser, Depends(get_current_user)],
    add_memeber: FamilyMemberSelect,
    session: Session = Depends(get_session),
) -> FamilyReadWithMembers:
    """
    添加家庭成员
    """
    family: DBFamily = current_user.family
    if not family:
        raise HTTPException(status_code=404, detail="user have no family")
    if family.owner_user_id != current_user.id:
        raise HTTPException(status_code=403, detail="only family owner can add member")
    if not add_memeber.username and not add_memeber.user_id:
        raise HTTPException(
            status_code=400, detail="username or user_id must be provided"
        )

    statement = select(DBUser)
    if add_memeber.user_id:
        statement = statement.where(DBUser.id == add_memeber.user_id)
    else:
        statement = statement.where(DBUser.username == add_memeber.username)
    user_model = session.exec(statement).first()
    if not user_model:
        raise HTTPException(status_code=404, detail="user not found")

    family.members.append(user_model)
    session.commit()
    session.refresh(family)
    return family


@router.delete("/user/family/member")
def delete_family_member(
    delete_member: FamilyMemberSelect,
    session: Session = Depends(get_session),
    current_user: DBUser = Depends(get_current_user),
) -> FamilyReadWithMembers:
    family = current_user.family
    if not family:
        raise HTTPException(status_code=404, detail="user have no family")
    if family.owner_user_id != current_user.id:
        raise HTTPException(status_code=403, detail="only family owner can add member")
    if not delete_member.username and not delete_member.user_id:
        raise HTTPException(
            status_code=400, detail="username or user_id must be provided"
        )
    statement = select(DBUser)
    if delete_member.user_id:
        statement = statement.where(DBUser.id == delete_member.user_id)
    else:
        statement = statement.where(DBUser.username == delete_member.username)
    user_model = session.exec(statement).first()
    if not user_model:
        raise HTTPException(status_code=404, detail="user not found")
    if user_model.family_id != family.id:
        raise HTTPException(status_code=403, detail="user not in family")
    user_model.family = None
    session.commit()
    session.refresh(family)
    return family
