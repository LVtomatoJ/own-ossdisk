from fastapi import HTTPException
from sqlmodel import Session
from oss2 import Auth, Bucket
from app.models.oss import DBOss
from app.routers.schemas.oss import OssAccountCreate
import oss2.exceptions


def get_bucket(oss_account: DBOss):
    try:
        auth = Auth(access_key_id=oss_account.ak, access_key_secret=oss_account.sk)
        bucket = Bucket(auth, oss_account.endpoint, oss_account.bucket_name)
    except Exception as e:
        raise HTTPException(status_code=400, detail="oss account error")
    return bucket


def check_oss_account(oss_account: OssAccountCreate):
    print(oss_account.model_dump())
    try:
        auth = Auth(access_key_id=oss_account.ak, access_key_secret=oss_account.sk)
        bucket = Bucket(auth, oss_account.endpoint, oss_account.bucket_name)
        info: oss2.models.GetBucketInfoResult = bucket.get_bucket_info()
        if info.extranet_endpoint != oss_account.endpoint:
            raise HTTPException(status_code=400, detail="oss endpoint error")
        return True
    except Exception as e:
        raise HTTPException(status_code=400, detail="oss account error")


def get_oss_objects_list(oss_account: DBOss, prefix: str):
    bucket = get_bucket(oss_account)
    list_objects: oss2.models.ListObjectsV2Result = bucket.list_objects_v2(
        delimiter="/", prefix=prefix
    )
    object_list: list[oss2.models.SimplifiedObjectInfo] = list_objects.object_list
    return object_list
