from dataclasses import dataclass

from ..block.rich_text import RichText
from .property import Property


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

    @staticmethod
    def from_dict(name: str, param: dict) -> "Text":
        try:
            rich_text = RichText.from_entity(param["rich_text"])
            id = param["id"]
            return Text(
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

    @classmethod
    def from_plain_text(cls, name: str, text: str):
        return cls(
            name=name,
            rich_text=RichText.from_plain_text(text=text),
        )

    @classmethod
    def empty(cls, name: str):
        return cls(
            name=name,
            rich_text=RichText.empty(),
        )

    @classmethod
    def _cast(cls, text_prop: "Text"):
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
