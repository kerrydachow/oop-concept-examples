"""
Open-Closed Principle
---------------------

-   This is an example of code that violates
    the open-closed principle.
-   As we add more shapes, we have to modify
    AreaCalculator to allow for the new shape.
"""


class Square:
    def __init__(self, side_length):
        self.side_length = side_length


class Circle:
    def __init__(self, radius):
        self.radius = radius


class AreaCalculator:
    def total_area(self, shapes: list) -> float:
        total = 0
        for shape in shapes:
            if isinstance(shape, Square):
                total += shape.side_length ** 2
            elif isinstance(shape, Circle):
                total += 3.14 * shape.radius ** 2
        return total
