from fastapi import FastAPI
from pydantic_settings import BaseSettings
from pydantic_core import MultiHostUrl
from pydantic import (
    PostgresDsn,
    computed_field,
)

class Settings(BaseSettings):
    postgres_db: str
    postgres_user: str
    postgres_password: str
    postgres_host: str
    postgres_port: int

    @computed_field
    @property
    def SQLALCHEMY_DATABASE_URI(self) -> PostgresDsn:
        return PostgresDsn.build(
            scheme="postgresql",
            username=self.postgres_user,
            password=self.postgres_password,
            host=self.postgres_host,
            port=self.postgres_port,
            path=self.postgres_db,
        ).unicode_string()

settings = Settings()
