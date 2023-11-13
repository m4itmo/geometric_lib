import math
from unittest import TestCase


def area(r):
    """
    Calculates the area of a circle based on its radius.

    Parameters:
    r (float): The radius of the circle.

    Returns:
    float: The area of the circle computed using the formula math.pi * r * r.
    """
    return math.pi * r * r


def perimeter(r):
    """
    Calculates the perimeter (circumference) of a circle based on its radius.

    Parameters:
    r (float): The radius of the circle.

    Returns:
    float: The perimeter (circumference) of the circle, computed using the formula 2 * math.pi * r.
    """
    return 2 * math.pi * abs(r)


class CircleTestCase(TestCase):
    # area
    def test_circle_zero_radius_area(self):
        self.assertEqual(area(0), 0)

    def test_circle_negative_radius_area(self):
        self.assertEqual(int(area(-10)), 314)

    def test_circle_area(self):
        self.assertEqual(int(area(10)), 314)

    # perimetr

    def test_circle_zero_radius_perimetr(self):
        self.assertEqual(perimeter(0), 0)

    def test_circle_negative_radius_perimetr(self):
        self.assertEqual(int(perimeter(-10)), 62)

    def test_circle_perimetr(self):
        self.assertEqual(int(perimeter(10)), 62)
