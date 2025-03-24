# from api.v1.endpoints.router import game
# from db.session import delete_tables, create_tables
from fastapi import FastAPI

from contextlib import asynccontextmanager

from database.session import create_tables, delete_tables
from producer_back.app.api.v1.endpoints.router import game


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("Таблицы Дропнулись")
    await create_tables()
    print("Таблицы создались")
    yield
    print("Выключение")

app = FastAPI(lifespan=lifespan)
app.include_router(game)
