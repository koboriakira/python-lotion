from typing import Any, Type, TypeVar, cast
from .lotion import Lotion
from .base_page import BasePage

P = TypeVar("P")


def lotion(database_id: str):
    """
    クラスデコレータ: データベースIDを引数として受け取り、
    自動的に BasePage を継承させ、アノテーションの属性をプロパティ化する。
    """

    def decorator(cls):
        # 元の初期化をオーバーライドしてアノテーション属性をプロパティ化
        original_init = getattr(cls, "__init__", lambda self: None)

        def new_init(self, *args, **kwargs):
            original_init(self, *args, **kwargs)

            # クラスアノテーションに基づいてプロパティを設定
            for attr_name, attr_type in cls.__annotations__.items():

                def make_getter(name, typ: Type[P]):
                    def getter(self) -> Any:
                        # print(typ, name)  # デバッグ出力
                        result = self.get(typ)  # `self.get()` は任意の実装
                        return cast(typ, result)

                    return getter

                setattr(cls, attr_name, property(make_getter(attr_name, attr_type)))

        # デコレータ引数で渡された database_id をクラス属性として設定
        setattr(cls, "DATABASE_ID", database_id)

        cls.__init__ = new_init
        cls.__module__ = cls.__module__

        return cls

    return decorator


__all__ = ["Lotion", "BasePage", "lotion"]
