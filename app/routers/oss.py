from typing import Annotated
from fastapi import APIRouter, Depends
from fastapi.params import Query
from sqlmodel import Field

from app.dependencies.oss import get_oss_db
from app.models.oss import DBOss
from app.routers.schemas.oss import OssObjectBase
from app.routers.utils.oss import get_oss_objects_list


router = APIRouter()


@router.get("/oss/{oss_id}/list", response_model=list[OssObjectBase])
def list_oss(
    prefix: Annotated[str | None, Query(max_length=50, regex=".+/$")] = "",
    oss_model: DBOss = Depends(get_oss_db),
):
    list = get_oss_objects_list(oss_model, prefix)
    return list
