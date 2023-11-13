from unittest import TestCase


def area(a, b):
    """
    Calculates the area of a rectangle based on its dimensions.

    Parameters:
    a (float): The length of one side of the rectangle.
    b (float): The length of the other side of the rectangle.

    Returns:
    float: The area of the rectangle, computed using the formula a * b.
    """
    return abs(a * b)


def perimeter(a, b):
    """
    Calculates the perimeter of a rectangle based on its dimensions.

    Parameters:
    a (float): The length of one side of the rectangle.
    b (float): The length of the other side of the rectangle.

    Returns:
    float: The perimeter of the rectangle, computed using the formula (a + b) * 2.
    """
    if a == 0 or b == 0:
        return 0
    return (abs(a) + abs(b)) * 2


class RectangleTestCase(TestCase):
    # area
    def test_rectangle_zero_side_area(self):
        self.assertEqual(area(10, 0), 0)

    def test_rectangle_negative_side_area(self):
        self.assertEqual(area(10, -10), 100)

    def test_rectangle_area(self):
        self.assertEqual(area(10, 10), 100)

    # perimetr

    def test_rectangle_zero_side_perimetr(self):
        self.assertEqual(perimeter(10, 0), 0)

    def test_rectangle_negative_side_perimetr(self):
        self.assertEqual(perimeter(10, -10), 40)

    def test_rectangle_perimetr(self):
        self.assertEqual(perimeter(10, 10), 40)
