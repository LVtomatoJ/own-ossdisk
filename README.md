
# 启动

## backend

poetry shell
poetry install
uvicorn app.main:app --reload

## frontend

cd own-ossdisk
bun install
bun run dev

# 须知

生成sk:
openssl rand -hex 32

# 文档地址

FastApi: <https://fastapi.tiangolo.com/zh/learn/>
Uvicorn: <https://www.uvicorn.org/>
SQLModel: <https://sqlmodel.tiangolo.com/>
Poetry: <https://python-poetry.org/>
AliyunOSS <https://aliyun-oss-python-sdk.readthedocs.io/en/latest/>
