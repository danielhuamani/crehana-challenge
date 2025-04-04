from collections.abc import Generator

import pytest
from fastapi.testclient import TestClient
from pydantic import PostgresDsn
from sqlmodel import Session, SQLModel, create_engine, delete

from src.core.session import get_db
from src.core.settings import settings
from src.main import app
from src.tasks.models import Task

postgres_uri = PostgresDsn.build(
    scheme="postgresql",
    username=settings.postgres_user,
    password=settings.postgres_password,
    host=settings.postgres_host,
    port=settings.postgres_port,
    path=f"{settings.postgres_db}_test",
).unicode_string()
test_engine = create_engine(str(postgres_uri))


def override_get_db() -> Generator[Session, None, None]:
    with Session(test_engine) as session:
        yield session


@pytest.fixture(scope="session", autouse=True)
def setup_test_db():
    SQLModel.metadata.create_all(test_engine)


@pytest.fixture(scope="module")
def client():
    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as c:
        yield c
    app.dependency_overrides.clear()


@pytest.fixture(scope="session", autouse=True)
def db() -> Generator[Session, None, None]:
    with Session(test_engine) as session:
        yield session
        statement = delete(Task)
        session.execute(statement)
        session.commit()


@pytest.fixture(autouse=True, scope="function")
def clean_db(db: Session):
    db.execute(delete(Task))
    db.commit()
