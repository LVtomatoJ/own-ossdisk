from contextlib import asynccontextmanager
from fastapi import FastAPI
from sqlmodel import SQLModel

from app.routers import common, oss, user
from app.database import engine


@asynccontextmanager
async def lifespan(_: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield


app = FastAPI(lifespan=lifespan)


app.include_router(common.router)
app.include_router(user.router)
app.include_router(oss.router)


@app.get("/")
def read_root():
    return "Hello, World!"
