import math


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
