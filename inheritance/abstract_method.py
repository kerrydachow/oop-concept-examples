"""
Abstract Method
-------------------

-   Decorating a class method with @abc.abstractmethod ensures that
    every subclass of X must implement that method.
-   Otherwise a TypeError will occur.
"""


import abc

class Bird(abc.ABC):
    @abc.abstractmethod
    def fly(self):
        print("Look at me, I am flying~")


class Parrot(Bird):
    pass


def example_1():
    try:
        parrot = Parrot()
    except TypeError as e:
        print(f"{e.__class__.__name__}: {e}")


class Penguin(Bird):
    def fly(self):
        print("I actually can't fly...")


def example_2():
    penguin = Penguin()
    penguin.fly()


if __name__ == "__main__":
    example_1()
    example_2()
