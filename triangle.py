def area(a, h):
    """
    Calculates the area of a triangle based on its base and height.

    Parameters:
    a (float): The length of the base of the triangle.
    h (float): The height of the triangle (perpendicular to the base).

    Returns:
    float: The area of the triangle, computed using the formula (a * h) / 2.
    """
    return a * h / 2

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
    return a + b + c
