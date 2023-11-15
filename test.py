from unittest import TestCase, main
from circle import area as circle_area, perimeter as circle_perimeter
from rectangle import area as rectangle_area, perimeter as rectangle_perimeter
from square import area as square_area, perimeter as square_perimeter
from triangle import area as triangle_area, perimeter as triangle_perimeter


class CircleTestCase(TestCase):
    # area
    def test_circle_zero_radius_area(self):
        self.assertEqual(circle_area(0), 0)

    def test_circle_negative_radius_area(self):
        self.assertEqual(int(circle_area(-10)), 314)

    def test_circle_area(self):
        self.assertEqual(int(circle_area(10)), 314)

    # perimetr
    def test_circle_zero_radius_perimetr(self):
        self.assertEqual(circle_perimeter(0), 0)

    def test_circle_negative_radius_perimetr(self):
        self.assertEqual(int(circle_perimeter(-10)), 62)

    def test_circle_perimetr(self):
        self.assertEqual(int(circle_perimeter(10)), 62)


class RectangleTestCase(TestCase):
    # area
    def test_rectangle_zero_side_area(self):
        self.assertEqual(rectangle_area(10, 0), 0)

    def test_rectangle_negative_side_area(self):
        self.assertEqual(rectangle_area(10, -10), 100)

    def test_rectangle_area(self):
        self.assertEqual(rectangle_area(10, 10), 100)

    # perimetr
    def test_rectangle_zero_side_perimetr(self):
        self.assertEqual(rectangle_perimeter(10, 0), 0)

    def test_rectangle_negative_side_perimetr(self):
        self.assertEqual(rectangle_perimeter(10, -10), 40)

    def test_rectangle_perimetr(self):
        self.assertEqual(rectangle_perimeter(10, 10), 40)


class SquareTestCase(TestCase):
    # area
    def test_square_zero_side_area(self):
        self.assertEqual(square_area(0), 0)

    def test_square_negative_side_area(self):
        self.assertEqual(square_area(-10), 100)

    def test_square_area(self):
        self.assertEqual(square_area(10), 100)

    # perimetr
    def test_square_zero_side_perimetr(self):
        self.assertEqual(square_perimeter(0), 0)

    def test_square_negative_side_perimetr(self):
        self.assertEqual(square_perimeter(-10), 40)

    def test_square_perimetr(self):
        self.assertEqual(square_perimeter(10), 40)


class TriangleTestCase(TestCase):
    # area
    def test_triangle_zero_side_area(self):
        self.assertEqual(triangle_area(0, 10), 0)
        self.assertEqual(triangle_area(10, 0), 0)

    def test_triangle_negative_side_area(self):
        self.assertEqual(triangle_area(10, -10), 50)
        self.assertEqual(triangle_area(-10, 10), 50)

    def test_triangle_area(self):
        self.assertEqual(triangle_area(10, 10), 50)

    # perimetr

    def test_triangle_zero_side_perimetr(self):
        self.assertEqual(triangle_perimeter(0, 10, 10), 0)
        self.assertEqual(triangle_perimeter(10, 0, 10), 0)
        self.assertEqual(triangle_perimeter(10, 10, 0), 0)

    def test_triangle_negative_side_perimetr(self):
        self.assertEqual(triangle_perimeter(-10, 10, 10), 30)
        self.assertEqual(triangle_perimeter(10, -10, 10), 30)
        self.assertEqual(triangle_perimeter(10, 10, -10), 30)

    def test_triangle_perimetr(self):
        self.assertEqual(triangle_perimeter(10, 10, 10), 30)


if __name__ == '__main__':
    main()
