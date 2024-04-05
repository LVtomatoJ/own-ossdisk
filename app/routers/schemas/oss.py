from enum import Enum
from typing import Optional
from pydantic import BaseModel


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
