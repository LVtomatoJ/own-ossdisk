from fastapi import HTTPException
from sqlmodel import Session
from oss2 import Auth, Bucket
from app.routers.schemas.oss import OssAccountCreate
import oss2.exceptions


def check_oss_account(oss_account: OssAccountCreate):
    print(oss_account.model_dump())
    try:
        auth = Auth(access_key_id=oss_account.ak, access_key_secret=oss_account.sk)
        bucket = Bucket(auth, oss_account.endpoint, oss_account.bucket_name)
        info: oss2.models.GetBucketInfoResult = bucket.get_bucket_info()
        return True
    except Exception as e:
        raise HTTPException(status_code=400, detail="oss account error")
