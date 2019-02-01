EPSILON = 1e-8


def is_zero(x) -> bool:
    return abs(x) < EPSILON


def is_equal(x, y) -> bool:
    return abs(x - y) < EPSILON
