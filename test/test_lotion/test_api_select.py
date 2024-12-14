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
        created_page = self.suite.create_page_in_database(
            database_id=self.DATABASE_ID, properties=[Title.from_plain_text(text="テスト")]
        )
        self.setup_page = self.suite.retrieve_page(page_id=created_page.page_id.value)
        return super().setUp()

    def test_セレクトを更新する(self):
        # Given
        select_prop = Select.from_plain_text(name="セレクト", text="セレクトA")
        properties = self.setup_page.properties.append_property(select_prop)

        # Then
        page_id = self.setup_page.page_id.value
        self.suite.update_page(page_id=page_id, properties=properties.values)
        actual = self.suite.retrieve_page(page_id=page_id)

        # When
        select = actual.get_select(name="セレクト")
        self.assertEqual(select.selected_name, "セレクトA")
