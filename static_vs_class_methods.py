"""
Static vs. Class Methods

-   Similarities:
    -   both are class level methods that are called on the class
    -   no need to instantiate an instance before calling the method
-   Differences:
    -   Static methods perform operation without access to static
        class variables
    -   Class methods perform operation with access to static class
        variables
"""


class Temperature:
    def __init__(self, temp_fahrenheit):
        self.temperature = temp_fahrenheit

    @classmethod
    def convert_to_celsius(cls, temp_fahrenheit):
        return (temp_fahrenheit - 32) * 5/9

    @staticmethod
    def convert_to_fahrenheit(temp_celsius):
        return (temp_celsius * 9/5) + 32


def main():
    temp = Temperature.convert_to_celsius(100)
    print(temp)
    temp = Temperature.convert_to_fahrenheit(temp)
    print(temp)


if __name__ == "__main__":
    main()
