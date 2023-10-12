"""
Open-Closed Principle
---------------------
-   Software entities should be open for extension, but closed for modification
-   In this example, we can add more shapes without ever needed to modify
    any other existing code.
-   We simply extend from the Shape class.
"""

from abc import ABC, abstractmethod

class Shape(ABC):
    """
    Abstract class of shapes.
    """
    @abstractmethod
    def area(self) -> float:
        """
        Shapes must be able to calculate their own area.
        :return: area
        """
        pass


class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self) -> float:
        return self.side_length ** 2


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self) -> float:
        return 3.14 * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height


class AreaCalculator:
    def total_area(self, shapes: list[Shape]) -> float:
        return sum(shape.area() for shape in shapes)
