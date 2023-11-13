from unittest import TestCase


def area(a, h):
    """
    Calculates the area of a triangle based on its base and height.

    Parameters:
    a (float): The length of the base of the triangle.
    h (float): The height of the triangle (perpendicular to the base).

    Returns:
    float: The area of the triangle, computed using the formula (a * h) / 2.
    """
    return abs(a * h / 2)


def perimeter(a, b, c):
    """
    Calculates the perimeter of a triangle based on its three sides.

    Parameters:
    a (float): The length of the first side of the triangle.
    b (float): The length of the second side of the triangle.
    c (float): The length of the third side of the triangle.

    Returns:
    float: The perimeter of the triangle, computed by adding the lengths of its three sides: a + b + c.
    """
    if a == 0 or b == 0 or c == 0:
        return 0
    return abs(a) + abs(b) + abs(c)


class TriangleTestCase(TestCase):
    # area
    def test_triangle_zero_side_area(self):
        self.assertEqual(area(0, 10), 0)
        self.assertEqual(area(10, 0), 0)

    def test_triangle_negative_side_area(self):
        self.assertEqual(area(10, -10), 50)
        self.assertEqual(area(-10, 10), 50)

    def test_triangle_area(self):
        self.assertEqual(area(10, 10), 50)

    # perimetr

    def test_triangle_zero_side_perimetr(self):
        self.assertEqual(perimeter(0, 10, 10), 0)
        self.assertEqual(perimeter(10, 0, 10), 0)
        self.assertEqual(perimeter(10, 10, 0), 0)

    def test_triangle_negative_side_perimetr(self):
        self.assertEqual(perimeter(-10, 10, 10), 30)
        self.assertEqual(perimeter(10, -10, 10), 30)
        self.assertEqual(perimeter(10, 10, -10), 30)

    def test_triangle_perimetr(self):
        self.assertEqual(perimeter(10, 10, 10), 30)
