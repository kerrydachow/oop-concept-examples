"""
Method Overloading
------------------
-   Python does not support traditional method overloading like Java or C++.
-   In Python, if you define multiple methods with the same name, the last
    one defined is will override the previous ones.
-   Python provides 2 mechanisms to achieve method overloading:
    1.  Default Arguments
    2.  Variable-Length Argument Lists
-   It is not true method overloading, but it leverages Python's dynamic
    typing system to achieve a similar result.
"""


class DefaultArguments:
    def method(self, a, b=None):
        if b is None:
            return a * 2
        return a + b


class VariableLength:
    def method(self, *args):
        if len(args) == 1:
            return args[0] * 2
        elif len(args) == 2:
            return args[0] + args[1]
        else:
            ans = 0
            for arg in args:
                ans += arg
            return ans


def default_arguments_example():
    obj = DefaultArguments()
    print(obj.method(10))
    print(obj.method(10, 20))


def variable_length_example():
    obj = VariableLength()
    print(obj.method(10))
    print(obj.method(10, 20))
    print(obj.method(10, 20, 30, 40, 50))


def main():
    print("Default Arguments Example\n------------------------")
    default_arguments_example()
    print("\nVariable Length Argument Lists "
          "Example\n-------------------------")
    variable_length_example()


if __name__ == "__main__":
    main()
