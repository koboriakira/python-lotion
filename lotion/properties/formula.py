from dataclasses import dataclass

from lotion.properties.property import Property


@dataclass
class Formula(Property):
    """Formula class

    ex.
    {'id': 'h_pG', 'type': 'formula', 'formula': {'type': 'number', 'number': 50}}
    """

    _formula: dict | None = None

    def __init__(
        self,
        name: str,
        id: str | None = None,  # noqa: A002
        formula: dict | None = None,
    ) -> None:
        self.name = name
        self.id = id
        self._formula = formula

    @staticmethod
    def of(key: str, param: dict) -> "Formula":
        return Formula(
            id=param["id"],
            name=key,
            formula=param["formula"],
        )

    @property
    def type(self) -> str:
        return "formula"

    def __dict__(self) -> dict:
        result = {
            "id": self.id,
            "type": self.type,
            "formula": self._formula,
        }
        return {
            self.name: result,
        }

    def value_for_filter(self) -> str:
        raise NotImplementedError
