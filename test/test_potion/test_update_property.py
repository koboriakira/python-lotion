from unittest import TestCase

import pytest

from potion import Potion
from properties.number import Number
from properties.property import Property
from properties.status import Status
from properties.text import Text
from properties.title import Title


class TestUpdateProperty(TestCase):
    DATABASE_ID = "1596567a3bbf80d58251f1159e5c40fa"

    def setUp(self) -> None:
        self.suite = Potion.get_instance()
        created_page = self.suite.create_page_in_database(
            database_id=self.DATABASE_ID, properties=[Title.from_plain_text(text="テスト")]
        )
        self.page = self.suite.retrieve_page(page_id=created_page["id"])
        return super().setUp()

    def tearDown(self) -> None:
        self.suite.remove_page(self.page.page_id.value)
        return super().setUp()

    @pytest.mark.post_api()
    def test_名前を変更する(self):
        title = Title.from_plain_text(text="テスト")
        actual = self._update_page(property=title)
        self.assertEqual(actual.get_title().text, "テスト")

    @pytest.mark.post_api()
    def test_テキストを変更する(self):
        text_prop = Text.from_plain_text(name="テキスト", text="テスト")
        actual = self._update_page(property=text_prop)
        self.assertEqual(actual.get_text(name="テキスト").text, "テスト")

    @pytest.mark.post_api()
    def test_数値を変更する(self):
        number_prop = Number.from_num(name="数値", value=1)
        actual = self._update_page(property=number_prop)
        self.assertEqual(actual.get_number(name="数値").number, 1)

    @pytest.mark.post_api()
    def test_セレクトを変更する(self):
        self.fail("ユーザが名前ベースでセレクトを選べるようにしたい")

    @pytest.mark.post_api()
    def test_マルチセレクトを変更する(self):
        self.fail("ユーザが名前ベースでマルチセレクトを選べるようにしたい")

    @pytest.mark.post_api()
    @pytest.mark.current()
    def test_ステータスを変更する(self):
        status_prop = Status.from_status_name(name="ステータス", status_name="未着手")
        actual = self._update_page(property=status_prop)
        self.assertEqual(actual.get_status(name="ステータス").status_name, "未着手")

    def _update_page(self, property: Property):
        # When
        properties = self.page.properties.append_property(property)
        self.suite.update_page(page_id=self.page.page_id.value, properties=properties.values)

        # Then
        return self.suite.retrieve_page(page_id=self.page.page_id.value)
