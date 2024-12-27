from dataclasses import dataclass
from typing import Type, TypeVar

from ..block.rich_text import RichText
from .property import Property

T = TypeVar("T", bound="Text")


@dataclass
class Text(Property):
    rich_text: RichText
    type: str = "rich_text"

    def __init__(
        self,
        name: str,
        rich_text: RichText,
        id: str | None = None,
    ) -> None:  # noqa: A002
        self.name = name
        self.id = id
        self.rich_text = rich_text

    @classmethod
    def from_dict(cls: Type[T], name: str, param: dict) -> T:
        try:
            rich_text = RichText.from_entity(param["rich_text"])
            id = param["id"]
            return cls(
                name=name,
                id=id,
                rich_text=rich_text,
            )
        except Exception as e:
            print(param)
            raise e

    def __dict__(self):
        result = {
            "type": self.type,
            "rich_text": self.rich_text.to_dict(),
        }
        return {self.name: result}

    def append_text(self, text: str):
        updated_text = self.text + "\n" + text
        cls = self.__class__
        return cls(
            name=self.name,
            rich_text=RichText.from_plain_text(updated_text.strip()),
        )

    @classmethod
    def from_plain_text(cls: Type[T], name: str, text: str) -> T:
        return cls(
            name=name,
            rich_text=RichText.from_plain_text(text=text),
        )

    @classmethod
    def empty(cls: Type[T], name: str) -> T:
        return cls(
            name=name,
            rich_text=RichText.empty(),
        )

    @classmethod
    def _cast(cls: Type[T], text_prop: "Text") -> T:
        return cls(
            name=text_prop.name,
            rich_text=text_prop.rich_text,
            id=text_prop.id,
        )

    @property
    def text(self) -> str:
        return self.rich_text.to_plain_text()

    def value_for_filter(self) -> str:
        raise NotImplementedError
