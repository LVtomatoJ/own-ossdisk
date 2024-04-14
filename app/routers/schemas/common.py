from pydantic import BaseModel


class LoginReq(BaseModel):
    username: str
    password: str


class TokenUser(BaseModel):
    username: str


class TokenData(BaseModel):
    username: str


class UserRead(BaseModel):
    id: int
    username: str
