import pytest

from lotion.recipe import CreateRecipe, Ingredient
from lotion.block import BulletedListItem, Heading, NumberedListItem
from lotion.properties.title import Title
from lotion.properties.url import Url


class TestIngredient:
    def test_to_text(self):
        # Given
        ingredient = Ingredient(name="絹豆腐", quantity="150g")

        # When
        result = ingredient.to_text()

        # Then
        assert result == "絹豆腐: 150g"


class TestCreateRecipe:
    def test_from_dict_with_full_data(self):
        # Given
        data = {
            "type": "Recipe",
            "title": "きな粉蒸しパン",
            "reference_url": "https://example.com/recipe",
            "ingredients": [
                {"name": "絹豆腐", "quantity": "150g"},
                {"name": "きな粉", "quantity": "50g"},
            ],
            "steps": [
                "ボウルに絹豆腐を入れる",
                "きな粉を加えて混ぜる",
            ],
        }

        # When
        recipe = CreateRecipe.from_dict(data)

        # Then
        assert recipe.title == "きな粉蒸しパン"
        assert recipe.reference_url == "https://example.com/recipe"
        assert len(recipe.ingredients) == 2
        assert recipe.ingredients[0].name == "絹豆腐"
        assert recipe.ingredients[0].quantity == "150g"
        assert len(recipe.steps) == 2

    def test_from_dict_without_optional_fields(self):
        # Given
        data = {
            "title": "シンプルレシピ",
        }

        # When
        recipe = CreateRecipe.from_dict(data)

        # Then
        assert recipe.title == "シンプルレシピ"
        assert recipe.reference_url is None
        assert recipe.ingredients == []
        assert recipe.steps == []

    def test_build_properties_with_url(self):
        # Given
        recipe = CreateRecipe(
            title="テストレシピ",
            reference_url="https://example.com",
        )

        # When
        properties = recipe.build_properties()

        # Then
        assert len(properties) == 2
        title_prop = properties[0]
        assert isinstance(title_prop, Title)
        assert title_prop.text == "テストレシピ"

        url_prop = properties[1]
        assert isinstance(url_prop, Url)
        assert url_prop.url == "https://example.com"

    def test_build_properties_without_url(self):
        # Given
        recipe = CreateRecipe(title="テストレシピ")

        # When
        properties = recipe.build_properties()

        # Then
        assert len(properties) == 1
        assert isinstance(properties[0], Title)

    def test_build_blocks(self):
        # Given
        recipe = CreateRecipe(
            title="テストレシピ",
            ingredients=[
                Ingredient(name="材料A", quantity="100g"),
                Ingredient(name="材料B", quantity="50ml"),
            ],
            steps=[
                "手順1を実行",
                "手順2を実行",
            ],
        )

        # When
        blocks = recipe.build_blocks()

        # Then
        # 材料セクション: Heading(1) + BulletedListItem(2) = 3
        # 手順セクション: Heading(1) + NumberedListItem(2) = 3
        assert len(blocks) == 6

        # 材料セクション
        assert isinstance(blocks[0], Heading)
        assert blocks[0].rich_text.to_plain_text() == "材料"

        assert isinstance(blocks[1], BulletedListItem)
        assert blocks[1].rich_text.to_plain_text() == "材料A: 100g"

        assert isinstance(blocks[2], BulletedListItem)
        assert blocks[2].rich_text.to_plain_text() == "材料B: 50ml"

        # 手順セクション
        assert isinstance(blocks[3], Heading)
        assert blocks[3].rich_text.to_plain_text() == "手順"

        assert isinstance(blocks[4], NumberedListItem)
        assert blocks[4].rich_text.to_plain_text() == "手順1を実行"

        assert isinstance(blocks[5], NumberedListItem)
        assert blocks[5].rich_text.to_plain_text() == "手順2を実行"

    def test_build_blocks_with_empty_ingredients_and_steps(self):
        # Given
        recipe = CreateRecipe(title="空のレシピ")

        # When
        blocks = recipe.build_blocks()

        # Then
        assert blocks == []

    def test_build_blocks_with_only_ingredients(self):
        # Given
        recipe = CreateRecipe(
            title="材料のみ",
            ingredients=[Ingredient(name="材料", quantity="100g")],
        )

        # When
        blocks = recipe.build_blocks()

        # Then
        assert len(blocks) == 2
        assert isinstance(blocks[0], Heading)
        assert isinstance(blocks[1], BulletedListItem)

    def test_build_blocks_with_only_steps(self):
        # Given
        recipe = CreateRecipe(
            title="手順のみ",
            steps=["手順1"],
        )

        # When
        blocks = recipe.build_blocks()

        # Then
        assert len(blocks) == 2
        assert isinstance(blocks[0], Heading)
        assert isinstance(blocks[1], NumberedListItem)
