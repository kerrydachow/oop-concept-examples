"""
Order of Initialization
----------------------------------

- super() must be explicitly called
"""

# Example 1.
class Animal:
    def __init__(self):
        print("Animal")


class Dog(Animal):
    def __init__(self):
        print("Dog")

print("Example 1:")
print("-------------------------")
dog = Dog()

# Example 2.
class Animal:
    def __init__(self):
        print("Animal")


class Dog(Animal):
    def __init__(self):
        super().__init__()
        print("Dog")

print("\nExample 2:")
print("-------------------------")
dog = Dog()

# Example 3.
class Animal:
    def __init__(self):
        print("Animal")


class Dog(Animal):
    def __init__(self):
        print("Dog")
        super().__init__()

print("\nExample 3:")
print("-------------------------")
dog = Dog()
