from abc import ABCMeta, abstractmethod
from dataclasses import dataclass
from typing import Type, TypeVar

P = TypeVar("P", bound="Property")

class Property(metaclass=ABCMeta):
    id: str | None
    name: str
    type: str = ""
    PROP_NAME = ""

    @abstractmethod
    def __dict__(self) -> dict:
        pass

    @abstractmethod
    def value_for_filter(self):  # noqa: ANN201
        pass

    @classmethod
    def _cast(cls: Type[P], prop: "Property") -> P:
        return cls(
            id=prop.id,
            name=prop.name,
        )
