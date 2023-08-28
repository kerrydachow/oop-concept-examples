"""
Data Hiding
-----------

-   Data hiding refers to restricting direct access from outside the class
-   Attributes are hidden to prevent direct modification
-   By providing controlled access through getters and setters, the
    internal state of the object is protected
-   Setters and getters allows for validation
-
"""


class Computer:
    def __init__(self, cpu: str, gpu: str):
        self.__cpu = cpu  # private attribute
        self.gpu = gpu

    @property
    def cpu(self):  # getter
        print("Getter!")
        return self.__cpu

    @cpu.setter
    def cpu(self, value):  # setter
        print("Setter!")
        self.__cpu = value


def main():
    my_pc = Computer("M1-CPU", "M1-GPU")

    # Setters & Getters
    print(my_pc.cpu)
    my_pc.cpu = "M2-CPU"
    print(my_pc.cpu)

    # Direct Access
    print(my_pc.gpu)
    my_pc.gpu = "M2-GPU"
    print(my_pc.gpu)


if __name__ == "__main__":
    main()
