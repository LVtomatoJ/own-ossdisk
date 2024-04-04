from sqlmodel import Session, create_engine
from app.models import user

engine = create_engine("sqlite:///database.db")


def get_session():
    with Session(engine) as session:
        yield session
