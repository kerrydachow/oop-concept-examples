"""
Operator Overloading
--------------------

-   Python supports operator overloading through magic methods.
-   These magic methods allow user-defined classes to implement and customize
    default behaviors.
-   The following example overrides the '+' operator for a custom 'Integer'
    class to change the behavior of `+` operator.
"""


class Integer:
    def __init__(self, value):
        self.value = value

    def __add__(self, other_integer):
        if isinstance(other_integer, Integer):
            return Integer(self.value + other_integer.value)
        raise NotImplementedError

    def __str__(self):
        return str(self.value)


def main():
    int1 = Integer(10)
    int2 = Integer(5)
    int3 = 3

    print(int1 + int2)
    try:
        print(int1 + int3)
    except NotImplementedError:
        print("Failed")


if __name__ == "__main__":
    main()
