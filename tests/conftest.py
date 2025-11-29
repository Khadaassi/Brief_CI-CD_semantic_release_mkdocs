from collections.abc import Generator

import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session, SQLModel, create_engine

import app.database
import app.main
from app.database import get_db

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
)


@pytest.fixture(scope="function")
def db() -> Generator[Session]:
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session
    SQLModel.metadata.drop_all(engine)


@pytest.fixture(scope="function")
def client(db: Session) -> Generator[TestClient]:
    def override_get_db() -> Generator[Session]:
        yield db

    original_engine = app.database.engine
    app.database.engine = engine
    app.main.engine = engine

    app.main.app.dependency_overrides[get_db] = override_get_db

    with TestClient(app.main.app, raise_server_exceptions=False) as test_client:
        yield test_client

    app.database.engine = original_engine
    app.main.engine = original_engine
    app.main.app.dependency_overrides.clear()
