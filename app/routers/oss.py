from pathlib import Path
from typing import Annotated
from fastapi import APIRouter, Depends
from fastapi.params import Query
from pydantic import UrlConstraints
from pydantic_core import Url
from sqlmodel import Field

from app.dependencies.oss import get_oss_db
from app.models.oss import DBOss
from app.routers.schemas.oss import DirPath, FilePath, OssObjectBase
from app.routers.utils.oss import get_object_download_url, get_oss_objects_list


router = APIRouter()


@router.get("/oss/{oss_id}/list", response_model=list[OssObjectBase])
def list_oss(
    prefix: DirPath = "",
    oss_model: DBOss = Depends(get_oss_db),
):
    list = get_oss_objects_list(oss_model, prefix)
    return list


@router.get(
    "/oss/{oss_id}/object",
    response_model=Annotated[Url, UrlConstraints(allowed_schemes=["http", "https"])],
)
def get_object(
    object_key: FilePath,
    expires: int = Query(3600, ge=1, le=3600),
    oss_model: DBOss = Depends(get_oss_db),
):
    download_url = get_object_download_url(oss_model, object_key, expires)
    return download_url


@router.delete(
    "/oss/{oss_id}/object",
)
def delete_object(
    object_key: FilePath,
    oss_model: DBOss = Depends(get_oss_db),
):
    delete_object(oss_model, object_key)
    return {"message": "delete success"}
