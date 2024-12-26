import functools
from typing import Any, cast

from lotion.base_page import BasePage
from lotion.properties.text import Text


def lotion(cls):
    """
    クラスデコレータ: 自動的に BasePage を継承させ、アノテーションの属性をプロパティ化する。
    元のクラス名やモジュール情報を保持する。
    """
    # BasePage を継承した新しいクラスを生成
    new_cls = type(
        cls.__name__,  # クラス名を元の名前にする
        (cls, BasePage),  # 元のクラスと BasePage を継承
        {},
    )

    # 元の初期化をオーバーライドしてアノテーション属性をプロパティ化
    original_init = getattr(new_cls, "__init__", lambda self: None)

    @functools.wraps(original_init)
    def new_init(self, *args, **kwargs):
        original_init(self, *args, **kwargs)  # 元の初期化を呼び出し

        for attr_name, attr_type in cls.__annotations__.items():
            # カスタムゲッターメソッドを生成
            def getter(self, t=attr_type) -> Any:
                result = self.get(t)
                return cast(t, result)

            # アノテーション属性にゲッターを設定
            setattr(new_cls, attr_name, property(getter))

    new_cls.__init__ = new_init

    # メタ情報を元のクラスに揃える
    new_cls.__module__ = cls.__module__

    return new_cls


class OriginalText(Text):
    PROP_NAME = "Text"


@lotion
class OriginalBasePage:
    original_text: OriginalText
