from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.ext.declarative import declarative_base
# from decouple import config

engine = create_async_engine(
    "postgresql+asyncpg://postgres:08092003@localhost/gifts"
)
new_session = async_sessionmaker(engine, expire_on_commit=False)

Model = declarative_base()


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)


async def delete_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.drop_all)
