from backend_app.main import add, subtract


def test_add() -> None:
    x: int = 1
    y: int = 4
    assert add(x, y) == x + y
    assert add(-x, y) == -x + y
    assert add(-y, y) == 0


def test_subtract() -> None:
    x: int = 15
    y: int = 3
    assert subtract(x, y) == x - y
    assert subtract(y, x) == y - x
    assert subtract(x, 0) == x
