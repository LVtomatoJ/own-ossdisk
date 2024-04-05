from sqlmodel import Session, create_engine
from app.models.user import DBUser
from app.models.oss import DBOss

engine = create_engine("sqlite:///database.db")


def get_session():
    with Session(engine) as session:
        yield session
