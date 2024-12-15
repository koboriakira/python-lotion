from typing import Any
from lotion.filter.condition import Prop, Cond


class ConditionRuleset:
    @staticmethod
    def validate(prop: Prop, cond: Cond, value: Any) -> None:
        ruleset = get_ruleset()
        if prop not in ruleset:
            raise ValueError(f"Property {prop} is not supported")
        if cond not in ruleset[prop]:
            raise ValueError(f"Condition {cond} is not supported for property {prop}")
        if type(value) not in ruleset[prop][cond]:
            raise ValueError(f"Value type {type(value)} is not supported for property {prop} with condition {cond}")


def get_ruleset() -> dict[Prop, dict[Cond, list[type]]]:
    result = {}
    result[Prop.TITLE] = {
        Cond.EQUALS: [str],
    }
    return result
