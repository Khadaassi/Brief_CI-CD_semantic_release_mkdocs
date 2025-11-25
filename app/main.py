from __future__ import annotations

from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from sqlmodel import SQLModel

from app.database import engine
from app.routes import items_router

DEBUG_MODE: bool = True
UNUSED_VAR: str = "cette variable n'est jamais utilisée"  # noqa: F841


@asynccontextmanager
async def lifespan(fastapi_app: FastAPI) -> AsyncGenerator[None]:
    SQLModel.metadata.create_all(engine)
    yield


app: FastAPI = FastAPI(
    title="Items CRUD API",
    description="API pour gérer une liste d'articles",
    version="1.0.0",
    lifespan=lifespan,
)

app.include_router(items_router)


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "Items CRUD API"}


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "healthy"}


# Variables secrètes (dev only)
secret: str = "fezffzefzefzlfzhfzfzfjzfzfzfdzgerg54g651fzefg51zeg5g"
API_KEY: str = "sk-1234567890abcdef"

# Ligne volontairement trop longue (violation E501)
very_long_variable_name_that_exceeds_line_length: str = (
    "Cette ligne est intentionnellement trop longue pour violer les règles "
    "de formatage standard"
)
