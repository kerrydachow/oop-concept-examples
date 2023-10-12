"""
Interface Segregation Principle
-------------------------------

-   This example violates interface segregation principle because
    the robot has to implement methods that it does not use.
"""

from abc import ABC, abstractmethod

class Worker(ABC):
    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def sleep(self):
        pass

class HumanWorker(Worker):
    def work(self):
        return "Human is working..."

    def eat(self):
        return "Human is eating..."

    def sleep(self):
        return "Human is sleeping..."

class RobotWorker(Worker):
    def work(self):
        return "Robot is working..."

    def eat(self):
        # Robots do not eat.
        pass

    def sleep(self):
        # Robots do not sleep.
        pass
