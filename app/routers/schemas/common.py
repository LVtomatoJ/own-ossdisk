from pydantic import BaseModel


class LoginReq(BaseModel):
    user_name: str
    password: str


class TokenUser(BaseModel):
    username: str


class TokenData(BaseModel):
    username: str
