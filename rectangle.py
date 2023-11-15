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
