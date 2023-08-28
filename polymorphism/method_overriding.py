"""
Method overriding
-----------------------------

-   Using method overriding to achieve polymorphism
"""


class Bird:
    def sound(self):
        return "Bird sound"


class Sparrow(Bird):
    def sound(self):
        return "Chirp"


class Crow(Bird):
    def sound(self):
        return "Caw"


def main():
    sparrow = Sparrow()
    crow = Crow()
    print(sparrow.sound())
    print(crow.sound())


if __name__ == "__main__":
    main()
