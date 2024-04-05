from fastapi import APIRouter, Depends

from app.dependencies.oss import get_oss_db
from app.models.oss import DBOss
from app.routers.utils.oss import get_oss_objects


router = APIRouter()


@router.get("/oss/{oss_id}/list")
def list_oss(oss_model: DBOss = Depends(get_oss_db)):
    get_oss_objects(oss_model)
    return {"oss_id": "ok"}
