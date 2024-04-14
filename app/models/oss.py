from sqlmodel import Relationship, SQLModel, Field

from app.routers.schemas.oss import OssStatusEnum, PlateFormEnum

from app.models.user import DBUser


class DBOss(SQLModel, table=True):

    __tablename__ = "oss_account"

    id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    user: DBUser = Relationship(back_populates="oss_accounts")
    ak: str
    sk: str
    plateform: PlateFormEnum
    endpoint: str
    bucket_name: str
    status: OssStatusEnum = Field(default=OssStatusEnum.normal.value)
