"""
Name Mangling
-------------

-   There are no access modifiers in Python as they are not Pythonic.
-   Therefore, developers must communicate with other developers by prefacing
    data attributes, or methods with underscores.
-   A single underscore indicates that the attribute, or method is for
    internal-use only. Similar to Java's Protected access modifier.
-   A dunder, or double underscore, indicates that the attribute or method
    should only be accessed within the class. Similar to Java's Private access
    modifier, but NOT equivalent.
-   Similar to Java, private methods should not be overridden by a subclass
    and this is enforced by the Python Interpreter by a mechanism called
    name mangling to prevent ACCIDENTAL method overriding.
-   Almost nothing in Python is truly private and with a little introspection,
    almost anything can be reached.
"""


class Dog:
    def __init__(self, name, age, breed):
        self._name = name
        self.__age = age
        self._breed = breed

    def get_age(self):
        return self.__age


class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def intro(self):
        print(f"I am {self.name} and I am {self.age} years old.")

    def __fact(self):
        print("Parents rock!")

    def speak(self):
        self.intro()
        self.__fact()


class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name, age)

    def intro(self):
        print("I am a child")

    def __fact(self):
        print("Parents SUCK!")

    def child_speak(self):
        self.__fact()


def private_attributes():
    charlie = Dog("Charlie", 5, "Golden Retriever")
    charlie.age = 10

    try:
        print(charlie.__age)
    except AttributeError:
        print("Could not access __age.")

    # Name mangling
    print(charlie._Dog__age)  # 5
    print(charlie.get_age())  # 5

    # Changing Charlie's age
    charlie._Dog__age = 10
    print(charlie.get_age())  # 10


def method_overriding():
    parent = Parent("John", 50)
    child = Child("Timmy", 10)
    child.speak()
    # >>> Parents rock!
    child.child_speak()


def main():
    print("Private Attributes name mangling example\n------------")
    private_attributes()
    print("\nMethod overriding with name mangling\n------------")
    method_overriding()


if __name__ == "__main__":
    main()
