"""
Liskov Substitution Principle
-----------------------------

-   This is example of code that violates Liskov Substitution Principle.
-   A square isn't truly a rectangle so when you modify a rectangles width
    but pass in a square instead, it leads to unexpected behaviors.
"""

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, new_width):
        self._width = new_width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, new_height):
        self._height = new_height


class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

    @Rectangle.width.setter
    def width(self, new_side_length):
        self._width = new_side_length
        self._height = new_side_length

    @Rectangle.height.setter
    def height(self, new_side_length):
        self._width = new_side_length
        self._height = new_side_length


def increase_rectangle_width(rectangle: Rectangle, val: int):
    """
    Increase the rectangles width only.

    :param rectangle: a rectangle
    :param val: a value
    :return: None
    """
    rectangle.width += val

square = Square(5)
increase_rectangle_width(square, 10)
print(square.width)  # 15
print(square.height)  # 15 - unexpected if you think you're working with just a rectangle
