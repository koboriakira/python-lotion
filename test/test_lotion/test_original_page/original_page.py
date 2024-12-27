import functools
from typing import Any, TypeVar, cast

from lotion.base_page import BasePage
from lotion.properties.text import Text


T = TypeVar("T")


def lotion(cls):
    """
    クラスデコレータ: 自動的に BasePage を継承させ、アノテーションの属性をプロパティ化する。
    元のクラス名やモジュール情報を保持する。
    """
    # 元の初期化をオーバーライドしてアノテーション属性をプロパティ化
    original_init = getattr(cls, "__init__", lambda self: None)

    def new_init(self, *args, **kwargs):
        original_init(self, *args, **kwargs)

        for attr_name, attr_type in cls.__annotations__.items():
            def getter(self) -> Any:  # 型情報を補足
                result = self.get(attr_type)
                return cast(attr_type, result)

            setattr(cls, attr_name, property(getter))

    cls.__init__ = new_init
    cls.__module__ = cls.__module__

    return cls


class OriginalText(Text):
    PROP_NAME = "Text"


@lotion
class OriginalBasePage(BasePage):
    original_text: OriginalText
