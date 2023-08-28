"""
Duck Typing
-----------

-   If it looks like a duck, swims like a duck, and quacks like a duck, then
    it probably is a duck.
-   No need for a formal interface or a specific superclass for objects
    to be treated polymorphically.
"""


class Cat:
    def sound(self):
        return "Meow"


class Dog:
    def sound(self):
        return "Woof"


def animal_sound(animal):
    return animal.sound()


def main():
    cat = Cat()
    dog = Dog()
    print(animal_sound(cat))  # Outputs: Meow
    print(animal_sound(dog))  # Outputs: Woof


if __name__ == "__main__":
    main()
