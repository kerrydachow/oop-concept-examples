"""
Observer Design Pattern
-----------------------

-   A number of observers that are observing something
-   That something is known as the core
-   When something changes, or some state has been reaches,
    the core notifies its observers by calling all the callbacks
    that were registered by them
-   Observers can choose what they want to do with the information
    notified by the core
-   Requirements
    1.  all observers implement either the same interface or a
        similar method. (accepts same parameters)
    2.  the core does not care who is observing or what they do
        when a change occurs
    3.  the core only runs callbacks to notify the observers
"""

from abc import ABC, abstractmethod
from enum import Enum


class Core(ABC):
    """
    The Core interface declares a set of methods for managing subscribers.
    """

    @abstractmethod
    def attach(self, observer) -> None:
        """
        Attach an observer.

        :param observer: an observer
        :return: None
        """
        pass

    @abstractmethod
    def detach(self, observer) -> None:
        """
        Detach an observer.

        :param observer: an observer
        :return: None
        """
        pass

    @abstractmethod
    def notify(self) -> None:
        """
        Notify all observers.

        :return: None
        """
        pass


class Observer(ABC):
    """
    The Observer interface declares a callback that is used by the core.
    """

    @abstractmethod
    def callback(self, core: Core) -> None:
        """
        A callback function used by the core when it is updated

        :param core: the core
        :return: None
        """
        pass


class ProfessorState(Enum):
    """
    Set of possible states for the professor
    """

    ASSIGN_NEW_HOMEWORK = "assigning new homework"
    ASKS_WHO_WANTS_FREE_MARKS = "asking who wants free marks"
    POP_QUIZ = "conducting a Pop quiz!"
    DISMISS_CLASS = "dismissing the class"
    SITTING_AT_DESK = "sitting at their desk..."
    CLEAN_UP = "cleaning up"




class Student(Observer):
    """
    A student.
    """

    def __init__(self, name):
        self.name = name

    def callback(self, core):
        if core.state == ProfessorState.ASKS_WHO_WANTS_FREE_MARKS:
            print(f"{self.name} raises hand!")
        else:
            print(f"{self.name} ignores Professor {core.name}")


class Professor(Core):
    """
    A professor.
    """

    def __init__(self, name):
        self.state = ProfessorState.SITTING_AT_DESK
        self.name = name
        self._observers = []

        print(f"Professor {self.name} is {self.state.value}")

    def notify(self) -> None:
        for o in self._observers:
            o.callback(self)

    def attach(self, o) -> None:
        self._observers.append(o)
        print(f"{o.name} is observing Professor {self.name}")

    def detach(self, o) -> None:
        self._observers.remove(o)
        print(f"{o.name} is no longer observing Professor {self.name}")

    def change_state(self, state: ProfessorState) -> None:
        self.state = state
        print(f"Professor {self.name} is {self.state.value}")
        self.notify()

# Instantiate
john = Professor("John")
kerry = Student("Kerry")
tom = Student("Tom")

# Observers observing core
john.attach(kerry)
john.attach(tom)
print()

john.change_state(ProfessorState.ASSIGN_NEW_HOMEWORK)
print()
john.change_state(ProfessorState.ASKS_WHO_WANTS_FREE_MARKS)
print()
john.change_state(ProfessorState.DISMISS_CLASS)
print()
john.detach(kerry)
print()
john.change_state(ProfessorState.CLEAN_UP)
print()
