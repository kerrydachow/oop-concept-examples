"""
Structural vs. Nominal Typing
---------------------------------

-   In Java, C#, C++, or other statically typed languages, we must specify
    the type of the object. This is known as nominal typing.
-   The type is then also checked at compile-time before fully compiled.
-   Python uses dynamic typing to determine the type of the objects
    during runtime.
-   Dynamic typing gives more flexibility but may introduce more bugs.
-   Opposed to nominal typing, Python uses structural typing.
-   If the internal structure both has what we're looking for, we can reuse
    a function for both different types.
-   This is known as runtime polymorphism:
    "We don't care what kind of object you are, as long as you have X Y Z"
"""

class Object1:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

class Object2:
    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z


def perform_operation(obj):
    return obj.x + obj.y


def main():
    obj_1 = Object1(10, 20)
    obj_2 = Object2(1, 2, 4)
    print(perform_operation(obj_1))  # 30
    print(perform_operation(obj_2))  # 3


if __name__ == "__main__":
    main()
