from dataclasses import dataclass
from typing import Type, TypeVar

from .property import Property

T = TypeVar("T", bound="Number")


@dataclass
class Number(Property):
    number: int | None
    type: str = "number"

    def __init__(
        self,
        name: str,
        id: str | None = None,  # noqa: A002
        number: int | None = None,
    ) -> None:
        self.name = name
        self.id = id
        self.number = number

    def add(self, count: int):
        prev = self.number if self.number is not None else 0
        cls = type(self)
        return cls(
            name=self.name,
            id=self.id,
            number=prev + count,
        )

    @classmethod
    def of(cls: Type[T], name: str, param: dict) -> T:
        if param["number"] is None:
            return cls(name=name, id=param["id"])
        return cls(
            name=name,
            id=param["id"],
            number=param["number"],
        )

    @classmethod
    def empty(cls: Type[T], name: str | None = None) -> T:
        return cls(name=name or cls.PROP_NAME)

    def is_empty(self) -> bool:
        return self.number is None

    @property
    def value(self) -> int:
        return self.number or 0

    def __dict__(self) -> dict:
        result = {
            "type": self.type,
            self.type: self.number,
        }
        if self.id is not None:
            result["id"] = self.id
        return {
            self.name: result,
        }

    @classmethod
    def from_num(cls: Type[T], value: int, name: str | None = None) -> T:
        return cls(
            name=name or cls.PROP_NAME,
            number=value,
        )

    def value_for_filter(self):
        return self.number
