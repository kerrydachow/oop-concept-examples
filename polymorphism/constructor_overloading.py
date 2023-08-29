"""
Constructor Overloading
------------------------

-   Python does not support traditional constructor overloading
-   If you write multiple __init__ methods, the last defined init will
    override the previous inits
-   There are 3 mechanisms to achieve constructor overloading:
    1.  Default Arguments
    2.  Variable-Length Arguments
    3.  Class Methods
"""


class DefaultArguments:
    def __init__(self, a=None, b=None):
        self.a = a
        self.b = b


class VariableLength:
    def __init__(self, *args):
        match len(args):
            case 0:
                self.a = None
                self.b = None
            case 1:
                self.a = args[0]
                self.b = None
            case 2:
                self.a, self.b = args


class ClassMethod:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @classmethod
    def create_empty_value(cls):
        return cls(None, None)

    @classmethod
    def create_single_value(cls, a):
        return cls(a, None)


def default_arguments_example():
    obj_1 = DefaultArguments()
    obj_2 = DefaultArguments(10)
    obj_3 = DefaultArguments(10, 20)


def variable_length_arguments_example():
    obj_1 = VariableLength()
    obj_2 = VariableLength(10)
    obj_3 = VariableLength(10, 20)


def class_method_example():
    obj_1 = ClassMethod.create_empty_value()
    obj_2 = ClassMethod.create_single_value(10)
    obj_3 = ClassMethod(10, 20)


def main():
    default_arguments_example()
    variable_length_arguments_example()
    class_method_example()


if __name__ == "__main__":
    main()
