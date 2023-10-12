"""
Interface Segregation Principle
-------------------------------

-   Clients shouldn't be forced to depend on interfaces or methods
    they do not use.
-   In this example, the robot does not depend on any interfaces
    that it does not use.
"""

from abc import ABC, abstractmethod

class Workable(ABC):
    @abstractmethod
    def work(self):
        pass

class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass

class Sleepable(ABC):
    @abstractmethod
    def sleep(self):
        pass

class HumanWorker(Workable, Eatable, Sleepable):
    def work(self):
        return "Human is working..."

    def eat(self):
        return "Human is eating..."

    def sleep(self):
        return "Human is sleeping..."

class RobotWorker(Workable):
    def work(self):
        return "Robot is working..."
