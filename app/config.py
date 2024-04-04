from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str = "sqlite+aiosqlite:///database.db"
    echo_sql: bool = True
    test: bool = False
    project_name: str = "My FastAPI project"
    token_secret: str = (
        "3503fafffd9729544732a36791e64f1978e57f1ff3f9900f95e611a5103613a0"
    )


settings = Settings()  # type: ignore
