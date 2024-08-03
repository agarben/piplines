# app/main.py
from click import secho


def add(a: int, b: int) -> int:
    return a + b


def subtract(a: int, b: int) -> int:
    return a - b


def print(s: str) -> None:
    secho(s, fg="green")
