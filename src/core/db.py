from sqlmodel import Session, create_engine, SQLModel

from src.tasks.models import Task
from src.core.settings import settings

engine = create_engine(str(settings.SQLALCHEMY_DATABASE_URI))


def create_db_and_tables() -> None:
    SQLModel.metadata.create_all(engine)
