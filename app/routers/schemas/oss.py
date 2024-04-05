from enum import Enum
from typing import Optional
from pydantic import BaseModel


class PlateFormEnum(str, Enum):
    aliyun = "aliyun"


class OssAccountCreate(BaseModel):
    ak: str
    sk: str
    plateform: PlateFormEnum
    user_id: Optional[int] = None


class OssAccountRead(BaseModel):
    id: int
    plateform: PlateFormEnum
