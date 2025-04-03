from typing import Union

from fastapi import FastAPI

app = FastAPI(title="Crehana Challenge")


@app.get("/")
def read_root():
    return {"Hello": "World"}


