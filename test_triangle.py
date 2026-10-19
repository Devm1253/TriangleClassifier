import math
from triangle import classify_triangle

#  Test that a triangle with a zero side is invalid
def test_zero_side():
    assert classify_triangle(0, 5, 5) == "Invalid"
    assert classify_triangle(5, 0, 5) == "Invalid"
    assert classify_triangle(5, 5, 0) == "Invalid"
 #Test that a triangle with negative sides is invalid
def test_negative_side():
    assert classify_triangle(-1, 5, 5) == "Invalid"
    assert classify_triangle(5, -1, 5) == "Invalid"
    assert classify_triangle(5, 5, -1) == "Invalid"
# Test that a triangle with sides that do not satisfy the triangle inequality is invalid
def test_triangle_inequality():
    assert classify_triangle(1, 2, 3) == "Invalid"
    assert classify_triangle(2, 3, 1) == "Invalid"
    assert classify_triangle(3, 1, 2) == "Invalid"  
    assert classify_triangle(1, 2, 4) == "Invalid"

def test_equilateral_triangle():
   assert classify_triangle(5, 5, 5) == "Equilateral" 

   # Test that a triangle with two equal sides is classified as isosceles
def test_isosceles_triangle():
   assert classify_triangle(5, 5, 3) == "Isosceles"
   assert classify_triangle(5, 3, 5) == "Isosceles"
   assert classify_triangle(3, 5, 5) == "Isosceles"

   # Test that a triangle with all sides different is classified as scalene
def test_scalene_triangle():
   assert classify_triangle(4, 5, 6) == "Scalene"
   assert classify_triangle(5, 6, 7) == "Scalene"
   assert classify_triangle(7, 8, 9) == "Scalene"

   # Test that a triangle with sides that satisfy the Pythagorean theorem is classified as right
def test_right_triangle():
   assert classify_triangle(3, 4, 5) == "Right Scalene" 
   assert classify_triangle(5, 12, 13) == "Right Scalene"
   assert classify_triangle(8, 15, 17) == "Right Scalene"
   assert classify_triangle(5, 5, 5 * math.sqrt(2)) == "Right Isosceles"