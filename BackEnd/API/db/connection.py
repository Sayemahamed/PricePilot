from typing import Any, AsyncGenerator

from API.config import settings
from click import echo
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.ext.asyncio.engine import AsyncEngine
from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession

async_engine: AsyncEngine = create_async_engine(
    url=settings.POSTGRES_URL_ASYNC, echo=True
)


async def init_db() -> None:
    async with async_engine.begin() as conn:
        from API.db.models import Price, Product, Tracking, User
        await conn.run_sync(SQLModel.metadata.create_all)


async def get_async_session() -> AsyncGenerator[AsyncSession, Any]:
    async_session = async_sessionmaker(
        bind=async_engine, class_=AsyncSession, expire_on_commit=False
    )
    async with async_session() as session:
        yield session
