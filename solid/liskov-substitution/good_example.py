"""
Liskov Substitution Principle
-----------------------------

-   Objects of a superclass shall be replaceable with objects of a subclass
    without affecting the correctness of the program
-   In this example Square and Rectangle are independent classes because
    logically, they're different objects. See bad example.
-   In many situations, it's more about understanding the true nature
    of the relationship between entities than just focusing on their apparent
    similarities.
"""

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

class Square:
    def __init__(self, side):
        self._side = side

    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, value):
        self._side = value


def increase_rectangle_width(rectangle: Rectangle, val: int):
    """
    Increase the rectangles width only.

    :param rectangle: a rectangle
    :param val: a value
    :return: None
    """
    rectangle.width += val

def increase_square_side(square: Square, val: int):
    """
    Increase the squares side.

    :param square: a square
    :param val: a value
    :return: None
    """
    square.width += val
