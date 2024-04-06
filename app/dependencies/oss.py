from typing import Annotated
from fastapi import Depends, HTTPException
from app.dependencies.auth import get_current_user
from app.dependencies.db import DBSessionDep
from sqlmodel import select

from app.models.oss import DBOss
from app.models.user import DBUser


def get_oss_db(
    oss_id: int,
    session: DBSessionDep,
    user_model: Annotated[DBUser, Depends(get_current_user)],
) -> DBOss:
    oss_model = session.exec(select(DBOss).where(DBOss.id == oss_id)).first()
    if not oss_model:
        raise HTTPException(status_code=400, detail="oss account not found")
    if oss_model.user_id != user_model.id:
        raise HTTPException(status_code=400, detail="oss account not belong to you")
    return oss_model
