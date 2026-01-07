from dataclasses import dataclass

from lotion.base_page import BasePage
from lotion.block import Block, BulletedListItem, Heading, NumberedListItem
from lotion.properties.property import Property
from lotion.properties.title import Title
from lotion.properties.url import Url


@dataclass
class Ingredient:
    """材料を表すデータクラス"""

    name: str
    quantity: str

    def to_text(self) -> str:
        """材料を「名前: 量」の形式でテキストに変換"""
        return f"{self.name}: {self.quantity}"


class CreateRecipe:
    """レシピページを作成するためのファクトリクラス"""

    def __init__(
        self,
        title: str,
        reference_url: str | None = None,
        ingredients: list[Ingredient] | None = None,
        steps: list[str] | None = None,
        title_prop_name: str = "名前",
        url_prop_name: str = "参照URL",
    ):
        self.title = title
        self.reference_url = reference_url
        self.ingredients = ingredients or []
        self.steps = steps or []
        self.title_prop_name = title_prop_name
        self.url_prop_name = url_prop_name

    @classmethod
    def from_dict(cls, data: dict) -> "CreateRecipe":
        """辞書データからCreateRecipeインスタンスを生成"""
        ingredients = [
            Ingredient(name=ing["name"], quantity=ing["quantity"])
            for ing in data.get("ingredients", [])
        ]
        return cls(
            title=data["title"],
            reference_url=data.get("reference_url"),
            ingredients=ingredients,
            steps=data.get("steps", []),
        )

    def build_properties(self) -> list[Property]:
        """レシピページのプロパティを構築"""
        properties: list[Property] = [
            Title.from_plain_text(self.title, name=self.title_prop_name),
        ]
        if self.reference_url:
            properties.append(Url.from_url(self.reference_url, name=self.url_prop_name))
        return properties

    def build_blocks(self) -> list[Block]:
        """レシピページのブロック（コンテンツ）を構築"""
        blocks: list[Block] = []

        # 材料セクション
        if self.ingredients:
            blocks.append(Heading.from_plain_text(2, "材料"))
            for ingredient in self.ingredients:
                blocks.append(BulletedListItem.from_plain_text(ingredient.to_text()))

        # 手順セクション
        if self.steps:
            blocks.append(Heading.from_plain_text(2, "手順"))
            for step in self.steps:
                blocks.append(NumberedListItem.from_plain_text(step))

        return blocks

    def build_page(self, database_id: str) -> BasePage:
        """レシピページを構築して返す

        Args:
            database_id: レシピを保存するNotionデータベースのID

        Returns:
            作成済みのBasePageインスタンス
        """
        # 動的にデータベースIDを設定したBasePageサブクラスを作成
        page = BasePage.create(
            properties=self.build_properties(),
            blocks=self.build_blocks(),
        )
        page.DATABASE_ID = database_id
        return page
