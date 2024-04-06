from enum import Enum
from typing import Annotated, Optional
from fastapi.params import Query
from pydantic import BaseModel, Field


class OssStatusEnum(str, Enum):
    normal = "normal"
    abnormal = "abnormal"


class PlateFormEnum(str, Enum):
    aliyun = "aliyun"


class OssAccountCreate(BaseModel):
    ak: str
    sk: str
    endpoint: str
    bucket_name: str
    plateform: PlateFormEnum
    user_id: Optional[int] = None


class OssAccountRead(BaseModel):
    id: int
    plateform: PlateFormEnum
    endpoint: str
    bucket_name: str
    status: OssStatusEnum


class OssObjectBase(BaseModel):
    key: str
    size: int
    last_modified: int


DirPath = Annotated[str | None, Query(regex=".+/$")]
FilePath = Annotated[str, Query(regex=".+")]
