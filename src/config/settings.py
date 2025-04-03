from fastapi import FastAPI
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    postgres_db: str
    postgres_user: str
    postgres_password: int
    postgres_host: str
    postgres_port: int

settings = Settings()
