"""
Dependency Inversion Principle
------------------------------

-   High-level modules should not depend on low-level modules. Both should
    depend on abstractions (e.g. interfaces).
-   Abstractions should not depend on details. Details should depend on abstractions.
-   DIP encourages us to write code that depends upon interfaces or abstract
    classes rather than concrete classes. This makes the system more modular,
    flexible, and easier to change and maintain.
-   This example is good because Switch now depends on an Abstract Class.
-   Therefore we can easily add more devices without modifying Switch class.
"""

from abc import ABC, abstractmethod

class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


class LightBulb(Switchable):
    def turn_on(self):
        return "LightBulb turned on"

    def turn_off(self):
        return "LightBulb turned off"


class CeilingFan(Switchable):
    def turn_on(self):
        return "CeilingFan turned on"

    def turn_off(self):
        return "CeilingFan turned off"


class Switch:
    def __init__(self, device: Switchable):
        self.device = device

    def operate(self):
        return self.device.turn_on() if True else self.device.turn_off()
