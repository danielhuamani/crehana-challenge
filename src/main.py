from logging import INFO, basicConfig, getLogger

from fastapi import FastAPI

from src.core.db import create_db_and_tables
from src.tasks import routes as task_routes

logger = getLogger(__name__)
basicConfig(level=INFO)
app = FastAPI(title="Crehana Challenge")


@app.on_event("startup")
def on_startup():
    logger.info("Starting up...")
    create_db_and_tables()
    logger.info("Shutting down...")
    logger.info("Finished shutting down.")


app.include_router(task_routes.router)
