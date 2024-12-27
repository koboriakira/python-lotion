from typing import Any, Type, TypeVar, cast
from .lotion import Lotion
from .base_page import BasePage

P = TypeVar("P")


def lotion(cls):
    """
    クラスデコレータ: 自動的に BasePage を継承させ、アノテーションの属性をプロパティ化する。
    元のクラス名やモジュール情報を保持する。
    """
    original_init = getattr(cls, "__init__", lambda self: None)

    def new_init(self, *args, **kwargs):
        original_init(self, *args, **kwargs)

        for attr_name, attr_type in cls.__annotations__.items():

            def make_getter(name, typ: Type[P]):
                def getter(self) -> Any:
                    result = self.get(typ)
                    return cast(P, result)

                return getter

            setattr(cls, attr_name, property(make_getter(attr_name, attr_type)))

    cls.__init__ = new_init
    cls.__module__ = cls.__module__

    return cls


__all__ = ["Lotion", "BasePage", "lotion"]
