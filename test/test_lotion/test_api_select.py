from unittest import TestCase

import pytest

from lotion import Lotion
from lotion.properties import Title
from lotion.properties import Select


@pytest.mark.api()
@pytest.mark.current()
class TestApiSelect(TestCase):
    DATABASE_ID = "15a6567a3bbf80b4a76fc106b37fb92f"

    def setUp(self) -> None:
        self.suite = Lotion.get_instance()

        select_a_prop = Select.of(
            name="セレクトA",
            param={
                "id": "oHJt",
                "type": "select",
                "select": {"id": "d9d95b7b-53e9-4497-8d8f-9aac9bb281ac", "name": "セレクトA", "color": "purple"},
            },
        )

    def test_すべての選択肢を取得する(self):
        # Then
        actual = self.suite.fetch_all_selects(
            database_id=self.DATABASE_ID,
        )

        # When: セレクトA、セレクトB、空白の2つの選択肢があること
        self.assertEqual(len(actual), 3)
        actual_select_names = [select.selected_name for select in actual]
        self.assertIn("セレクトA", actual_select_names)
        self.assertIn("セレクトB", actual_select_names)
        self.assertIn("", actual_select_names)

    def test_セレクトを更新する(self):
        # Given
        selects = self.suite.fetch_all_selects(database_id=self.DATABASE_ID)
        select_b_prop = [select for select in selects if select.selected_name == "セレクトB"][0]
        page = self.suite.create_page_in_database(
            database_id=self.DATABASE_ID, properties=[Title.from_plain_text(text="テスト")]
        )

        # When
        properties = page.properties.append_property(select_b_prop)
        self.suite.update_page(page_id=page.page_id.value, properties=properties.values)
        actual = self.suite.retrieve_page(page_id=page.page_id.value)

        # Then
        select = actual.get_select(name="セレクト")
        self.assertEqual(select.selected_name, "セレクトB")
