# app/main.py
from click import secho
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configure CORS
orig_origins = [
    "http://localhost",  # Allow this origin
    "http://localhost:80",  # Allow this origin (if your frontend is served from port 3000)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=orig_origins,  # Allows all origins (or specify only necessary origins)
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)


@app.get("/data")
def read_data():
    x = 5
    return {
        "message": f"Hello from backend container: {os.environ.get('HOSTNAME', 'DEFAULT_ENV')}"
    }


def add(a: int, b: int) -> int:
    return a + b


def subtract(a: int, b: int) -> int:
    return a - b


def print(s: str) -> None:
    secho(s, fg="green")
