import math

def is_valid_triangle(a, b, c) -> bool:
    """Return whether the sides form a non-degenerate triangle."""
    if a <= 0 or b <= 0 or c <= 0:
        return False
    if a + b <= c or a + c <= b or b + c <= a:
        return False
    return True


def classify_triangle(a, b, c) -> str:
    if not is_valid_triangle(a, b, c):
        return "Invalid"

    if a == b == c:
        shape = "Equilateral"
    elif a == b or b == c or a == c:
        shape = "Isosceles"
    else:
        shape = "Scalene"

    x, y, z = sorted([a, b, c])

    if math.isclose(x**2 + y**2, z**2, rel_tol=1e-9):
        return "Right " + shape

    return shape
