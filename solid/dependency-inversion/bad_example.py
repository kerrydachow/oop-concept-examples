"""
Dependency Inversion Principle
------------------------------

-   This example violates the Dependency Inversion Principle because
    changing Switch to control other devices means we must refactor
    Switch's implementation.
"""

class LightBulb:
    def turn_on(self):
        return "LightBulb turned on"

    def turn_off(self):
        return "LightBulb turned off"


class Switch:
    def __init__(self, bulb):
        self.bulb = bulb

    def operate(self):
        return self.bulb.turn_on() if True else self.bulb.turn_off()
