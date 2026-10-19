# Triangle Classifier

This Python program checks whether three sides form a triangle and returns
Equilateral, Isosceles, or Scalene. Invalid triangles return `Invalid`.
Right triangles have `Right ` before the shape, such as `Right Scalene`.
The right-angle calculation uses `math.isclose()` to allow for rounding.

## Run the tests

```sh
python -m pip install -r requirements.txt
python -m pytest -v
```

If using the project's virtual environment, activate it first:

```sh
source .venv/bin/activate
```

All 8 tests passed locally: 7 unit tests and 1 acceptance test.

## Equivalence classes and boundaries

- Invalid sides: zero or negative, such as `(0, 5, 5)` and `(-1, 5, 5)`.
- Invalid triangle inequality: `(1, 2, 4)`.
- Degenerate boundary: `(1, 2, 3)`, where two sides sum to the third.
- Equilateral: `(5, 5, 5)`.
- Isosceles: `(5, 5, 3)`.
- Scalene: `(4, 5, 6)`.
- Right scalene: `(3, 4, 5)`.
- Right isosceles with a non-integer side: `(5, 5, 5 * math.sqrt(2))`.

Some tests also change the side order to check that order does not affect the result.

## Why equilateral triangles cannot be right

For equal positive sides of length s, the Pythagorean theorem would require
s² + s² = s². This would require s = 0, which is not a valid triangle side.

## Copilot Review Log

I reviewed the Copilot test suggestions against the assignment's rules and
corrected the expected results where needed.

| Test                       | Copilot-suggested?                 | Kept / edited / rejected | Why                                                                                                                  |
| -------------------------- | ---------------------------------- | ------------------------ | -------------------------------------------------------------------------------------------------------------------- |
| Zero and negative sides    | Yes                     | Kept                     | Nonpositive sides must return `Invalid`.                                                                             |
| Triangle inequality        | Yes                     | Edited                   | Kept the equality boundary and added `(1, 2, 4)` for a sum smaller than the third side.                              |
| Equilateral and isosceles  | Yes                     | Kept                     | Expected labels matched the specification.                                                                           |
| Scalene                    | Yes                     | Edited                   | The draft expected `Scalene` for `(3, 4, 5)`. That is a right triangle, so I used `(4, 5, 6)` for this test instead. |
| Right triangle             | Yes                     | Edited                   | Changed the draft's `Right` expectations to `Right Scalene`, as required.                                            |
| Non-integer right triangle | No — added after other AI feedback | Added                    | Checked `(5, 5, 5 * math.sqrt(2))` returns `Right Isosceles`. Moved the assertion inside the test function.          |

## Acceptance criteria

1. Nonpositive sides or sides that fail the strict triangle inequality return
   `Invalid` without an exception.
2. Valid non-right triangles return the correct shape based on how many sides
   are equal: Equilateral, Isosceles, or Scalene.
3. Valid right triangles include the `Right ` prefix so the studio can identify
   pieces that need reinforced corners.

`test_acceptance.py` calls `classify_triangle()` with examples covering these
customer requirements in one test. An unexpected exception fails the test.

## AI-use disclosure

I used GitHub Copilot autocomplete to draft unit tests and reviewed the suggested
results against the specification.
