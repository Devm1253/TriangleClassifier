from triangle import classify_triangle


def test_stained_glass_requirements():
    cases = [
        ((0, 4, 5), "Invalid"),
        ((1, 2, 3), "Invalid"),
        ((5, 5, 5), "Equilateral"),
        ((5, 5, 3), "Isosceles"),
        ((4, 5, 6), "Scalene"),
        ((3, 4, 5), "Right Scalene"),
    ]

    for sides, expected in cases:
        assert classify_triangle(*sides) == expected
