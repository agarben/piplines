# app/main.py
from click import secho

from fastapi import FastAPI

app = FastAPI()


@app.get("/data")
def read_data():
    return {"message": "Hello from FastAPI"}


def add(a: int, b: int) -> int:
    return a + b


def subtract(a: int, b: int) -> int:
    return a - b


def print(s: str) -> None:
    secho(s, fg="green")
