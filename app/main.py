from __future__ import annotations

import os
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

SECRET_KEY: str = os.getenv("SECRET_KEY", "dev-only-not-for-production")
API_KEY: str | None = os.getenv("API_KEY")


# Ligne volontairement trop longue (violation E501)
very_long_variable_name_that_exceeds_line_length: str = (
    "Cette ligne est intentionnellement trop longue pour violer les règles "
    "de formatage standard"
)
