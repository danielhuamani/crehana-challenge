from contextlib import asynccontextmanager
from logging import INFO, basicConfig, getLogger

from fastapi import FastAPI

from src.core.db import create_db_and_tables
from src.tasks import routes as task_routes

logger = getLogger(__name__)
basicConfig(level=INFO)


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        logger.info("Starting up...")
        create_db_and_tables()
        yield
    finally:
        logger.info("Shutting down...")
        logger.info("Finished shutdown.")


app = FastAPI(title="Crehana Challenge", lifespan=lifespan)


app.include_router(task_routes.router)
