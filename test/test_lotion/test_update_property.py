from unittest import TestCase

import pytest

from lotion import Lotion
from lotion.properties.checkbox import Checkbox
from lotion.properties.number import Number
from lotion.properties.property import Property
from lotion.properties.status import Status
from lotion.properties.text import Text
from lotion.properties.title import Title
from lotion.properties.url import Url


@pytest.mark.api()
class TestUpdateProperty(TestCase):
    DATABASE_ID = "1596567a3bbf80d58251f1159e5c40fa"

    def setUp(self) -> None:
        self.suite = Lotion.get_instance()
        created_page = self.suite.create_page_in_database(
            database_id=self.DATABASE_ID, properties=[Title.from_plain_text(text="テスト")]
        )
        self.page = self.suite.retrieve_page(page_id=created_page.page_id.value)
        return super().setUp()

    def tearDown(self) -> None:
        self.suite.remove_page(self.page.page_id.value)
        return super().setUp()

    def test_名前を変更する(self):
        title = Title.from_plain_text(text="テスト")
        actual = self._update_page(property=title)
        self.assertEqual(actual.get_title().text, "テスト")

    def test_テキストを変更する(self):
        text_prop = Text.from_plain_text(name="テキスト", text="テスト")
        actual = self._update_page(property=text_prop)
        self.assertEqual(actual.get_text(name="テキスト").text, "テスト")

    def test_数値を変更する(self):
        number_prop = Number.from_num(name="数値", value=1)
        actual = self._update_page(property=number_prop)
        self.assertEqual(actual.get_number(name="数値").number, 1)

    def test_ファイルを変更する(self):
        self.skipTest("ファイルプロパティを作成するところから")

    def test_チェックボックスを変更する(self):
        checkbox_prop = Checkbox.true(name="チェックボックス")
        actual = self._update_page(property=checkbox_prop)
        self.assertEqual(actual.get_checkbox(name="チェックボックス").checked, True)

    def test_URLを変更する(self):
        url_prop = Url.from_url(name="URL", url="https://example.com")
        actual = self._update_page(property=url_prop)
        self.assertEqual(actual.get_url(name="URL").url, "https://example.com")

    def _update_page(self, property: Property):
        # When
        properties = self.page.properties.append_property(property)
        self.suite.update_page(page_id=self.page.page_id.value, properties=properties.values)

        # Then
        return self.suite.retrieve_page(page_id=self.page.page_id.value)
