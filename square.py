from unittest import TestCase


def area(a):
    """
    Calculates the area of a square based on the length of its side.

    Parameters:
    a (float): The length of one side of the square.

    Returns:
    float: The area of the square, computed using the formula a * a.
    """
    return abs(a * a)


def perimeter(a):
    """
    Calculates the perimeter of a square based on the length of its side.

    Parameters:
    a (float): The length of one side of the square.

    Returns:
    float: The perimeter of the square, computed using the formula 4 * a.
    """
    return abs(4 * a)


class SquareTestCase(TestCase):
    # area
    def test_square_zero_side_area(self):
        self.assertEqual(area(0), 0)

    def test_square_negative_side_area(self):
        self.assertEqual(area(-10), 100)

    def test_square_area(self):
        self.assertEqual(area(10), 100)

    # perimetr

    def test_square_zero_side_perimetr(self):
        self.assertEqual(perimeter(0), 0)

    def test_square_negative_side_perimetr(self):
        self.assertEqual(perimeter(-10), 40)

    def test_square_perimetr(self):
        self.assertEqual(perimeter(10), 40)
