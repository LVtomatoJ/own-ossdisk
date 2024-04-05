
# 启动

poetry shell
poetry install
uvicorn app.main:app --reload

# 须知

生成sk:
openssl rand -hex 32

# 文档地址

FastApi: <https://fastapi.tiangolo.com/zh/learn/>
Uvicorn: <https://www.uvicorn.org/>
SQLModel: <https://sqlmodel.tiangolo.com/>
Poetry: <https://python-poetry.org/>
