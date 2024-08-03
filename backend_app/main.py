# app/main.py
from click import secho
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configure CORS
orig_origins = [
    "http://localhost",  # Allow this origin
    "http://localhost:80",  # Allow this origin (frontend at port 80)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=orig_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/data")
def read_data():
    hostname = os.environ.get("HOSTNAME", "DEFAULT_ENV")
    return {"message": f"Hello from backend container: {hostname}"}


def add(a: int, b: int) -> int:
    return a + b


def subtract(a: int, b: int) -> int:
    return a - b


def print(s: str) -> None:
    secho(s, fg="green")
