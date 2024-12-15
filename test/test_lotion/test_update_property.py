from unittest import TestCase

import pytest

from lotion.properties.number import Number
from lotion.properties.text import Text
from lotion.properties.title import Title
from test.test_lotion.lotion_utils import create_empty_page, remove_page, update_page


@pytest.mark.api()
class TestUpdateProperty(TestCase):
    DATABASE_ID = "1596567a3bbf80d58251f1159e5c40fa"

    def setUp(self) -> None:
        self.page = create_empty_page(database_id=self.DATABASE_ID)
        return super().setUp()

    def tearDown(self) -> None:
        remove_page(page_id=self.page.page_id)
        return super().setUp()

    def test_名前を変更する(self):
        title = Title.from_plain_text(text="テスト")
        actual = update_page(page=self.page, property=title)
        self.assertEqual(actual.get_title().text, "テスト")

    def test_テキストを変更する(self):
        text_prop = Text.from_plain_text(name="テキスト", text="テスト")
        actual = update_page(page=self.page, property=text_prop)
        self.assertEqual(actual.get_text(name="テキスト").text, "テスト")

    def test_数値を変更する(self):
        number_prop = Number.from_num(name="数値", value=1)
        actual = update_page(page=self.page, property=number_prop)
        self.assertEqual(actual.get_number(name="数値").number, 1)

    def test_ファイルを変更する(self):
        self.skipTest("ファイルプロパティを作成するところから")
