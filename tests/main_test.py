from app.main import add


def test_add():
    x: int = 1
    y: int = 2
    assert add(x, y) == x + y
    assert add(-x, y) == -x + y
    assert add(-y, y) == 0
