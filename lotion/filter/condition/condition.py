from abc import ABCMeta, abstractmethod


class Condition(metaclass=ABCMeta):
    @abstractmethod
    def __dict__(self) -> dict:
        pass
