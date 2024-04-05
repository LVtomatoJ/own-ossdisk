from fastapi import HTTPException
from app.dependencies.db import DBSessionDep
from sqlmodel import select

from app.models.oss import DBOss


def get_oss_db(oss_id: int, session: DBSessionDep) -> DBOss:
    oss_model = session.exec(select(DBOss).where(DBOss.id == oss_id)).first()
    if not oss_model:
        raise HTTPException(status_code=400, detail="oss account not found")
    return oss_model
