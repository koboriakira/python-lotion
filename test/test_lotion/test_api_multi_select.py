from unittest import TestCase

import pytest

from lotion import Lotion
from lotion.properties import Title


@pytest.mark.api()
class TestApiMultiSelect(TestCase):
    DATABASE_ID = "15c6567a3bbf80818512f43db108616f"

    def setUp(self) -> None:
        self.suite = Lotion.get_instance()

    def test_すべての選択肢を取得する(self):
        # Then
        actual = self.suite.fetch_all_multi_select_elements(
            database_id=self.DATABASE_ID,
            name="マルチセレクト",
        )

        # When: A, B, C, Dの4つの選択肢がある
        print(actual)
        self.assertEqual(actual.size, 4)
        self.assertIsNotNone(actual.get("A"))
        self.assertIsNotNone(actual.get("B"))
        self.assertIsNotNone(actual.get("C"))
        self.assertIsNotNone(actual.get("D"))

    def test_セレクトを更新する(self):
        # Given
        page = self.suite.create_page_in_database(
            database_id=self.DATABASE_ID, properties=[Title.from_plain_text(text="テスト")]
        )

        # When
        multi_select_prop = self.suite.fetch_multi_select(
            database_id=self.DATABASE_ID, name="マルチセレクト", multi_select_names=["B", "D"]
        )
        properties = page.properties.append_property(multi_select_prop)
        self.suite.update_page(page_id=page.id, properties=properties.values)
        actual = self.suite.retrieve_page(page_id=page.id)

        # Then
        multi_select = actual.get_multi_select(name="マルチセレクト")
        multi_select_names = [value.name for value in multi_select.values]
        multi_select_names.sort()
        self.assertEqual(multi_select_names, ["B", "D"])
