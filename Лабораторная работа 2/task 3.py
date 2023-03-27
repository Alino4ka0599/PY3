def factorial_recursive(n: int) -> int:
    # базовый случай
    if n == 0:
        return 1
    # рекурсивный случай
    return n * factorial_recursive(n - 1)
