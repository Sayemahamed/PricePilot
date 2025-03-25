from contextlib import asynccontextmanager
from rich import print
from fastapi import FastAPI
from API.db import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("[green]Starting up...")
    await init_db()
    yield
    print("[green]Shutting down...")

version ="v1"
app = FastAPI(
    title="Price Pilot",
    lifespan=lifespan
    ,version=version,
    description="An AI-Powered E-Commerce Procurement Assistant",
    )