# geometric_lib

geometric_lib is a Python library for calculating geometric properties such as area and perimeter for various geometric shapes, including rectangles, squares, and triangles. The library provides convenient functions for performing calculations based on input parameters and returning the corresponding results.

## Table of Contents
1. [Project Description](#description)
2. [Functions](#functions)
3. [Change History](#change-history)

## Description
These functions are designed to be straightforward to use and can be incorporated into your Python programs or scripts to perform geometric calculations efficiently.
Here's a brief overview of the functions available in this project:

- Rectangle
  - `area(a, b)`: Calculates the area of a rectangle based on its dimensions.
  - `perimeter(a, b)`: Calculates the perimeter of a rectangle based on its dimensions.
- Square
  - `area(a)`: Calculates the area of a square based on the length of its side.
  - `perimeter(a)`: Calculates the perimeter of a square based on the length of its side.
- Triangle
  - `area(a, h)`: Calculates the area of a triangle based on its base and height.
  - `perimeter(a, b, c)`: Calculates the perimeter of a triangle based on its three sides.
- Circle
  - `area(r)`: Calculates the area of a circle based on its radius.
  - `perimeter(r)`: Calculates the perimeter (circumference) of a circle based on its radius.



## Functions

### rectangle `area(a, b)`

Calculates the area of a rectangle based on its dimensions.

Parameters:
- `a` (float): The length of one side of the rectangle.
- `b` (float): The length of the other side of the rectangle.

Returns:
- `float`: The area of the rectangle, computed using the formula `a * b`.

Example usage:
```python
result = area(5, 10)
print(result)  # Output: 50.0
```

### rectangle `perimeter(a, b)`

Calculates the perimeter of a rectangle based on its dimensions.

Parameters:
- `a` (float): The length of one side of the rectangle.
- `b` (float): The length of the other side of the rectangle.

Returns:
- `float`: The perimeter of the rectangle, computed using the formula `2 * (a + b)`.

Example usage:
```python
result = perimeter(5, 10)
print(result)  # Output: 30.0
```

### square `area(a)`

Calculates the area of a square based on the length of its side.

Parameters:
- `a` (float): The length of one side of the square.

Returns:
- `float`: The area of the square, computed using the formula `a * a`.

Example usage:
```python
result = area(5)
print(result)  # Output: 25.0
```

### square `perimeter(a)`

Calculates the perimeter of a square based on the length of its side.

Parameters:
- `a` (float): The length of one side of the square.

Returns:
- `float`: The perimeter of the square, computed using the formula `4 * a`.

Example usage:
```python
result = perimeter(5)
print(result)  # Output: 20.0
```

### triangle `area(a, h)`

Calculates the area of a triangle based on its base and height.

Parameters:
- `a` (float): The length of the base of the triangle.
- `h` (float): The height of the triangle (perpendicular to the base).

Returns:
- `float`: The area of the triangle, computed using the formula `(a * h) / 2`.

Example usage:
```python
result = area(5, 10)
print(result)  # Output: 25.0
```

### triangle `perimeter(a, b, c)`

Calculates the perimeter of a triangle based on its three sides.

Parameters:
- `a` (float): The length of the first side of the triangle.
- `b` (float): The length of the second side of the triangle.
- `c` (float): The length of the third side of the triangle.

Returns:
- `float`: The perimeter of the triangle, computed by adding the lengths of its three sides: `a + b + c`.

Example usage:
```python
result = perimeter(3, 4, 5)
print(result)  # Output: 12.0
```

### circle `area(r)`

Calculates the area of a circle based on its radius.

Parameters:
- `r` (float): The radius of the circle.

Returns:
- `float`: The area of the circle, computed using the formula `π * r * r`.

Example usage:
```python
result = area(5)
print(result)  # Output: 78.53981633974483
```

### circle `perimeter(r)`

Calculates the perimeter (circumference) of a circle based on its radius.

Parameters:
- `r` (float): The radius of the circle.

Returns:
- `float`: The perimeter (circumference) of the circle, computed using the formula `2 * π * r`.

Example usage:
```python
result = circle.perimeter(5)
print(result)  # Output: 31.41592653589793
```

## Change History

- `15f2e27`: Added `triangle.py` and fixed rectangle perimeter calculation.
- `2dfe381`: Added `rectangle.py`.
- `d078c8d`: Added documentation.
- `8ba9aeb`: Added support for circles and squares.

