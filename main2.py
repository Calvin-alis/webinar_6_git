
def add(a: int, b: int) -> int | str:
    return a + b

def minus(a: int, b:int) -> int | None:
    return a - b if isinstance(a, int) and isinstance(b, int) else None