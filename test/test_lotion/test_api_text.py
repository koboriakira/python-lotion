from unittest import TestCase

import pytest

from lotion.properties.text import Text
from test.test_lotion.lotion_utils import create_empty_page, remove_page, update_page


class OriginalText(Text):
    PROP_NAME = "Text"


@pytest.mark.api()
class TestApiText(TestCase):
    DATABASE_ID = "15d6567a3bbf80db8cb6d63ab1fecf22"

    def setUp(self) -> None:
        self.page = create_empty_page(database_id=self.DATABASE_ID)
        return super().setUp()

    def tearDown(self) -> None:
        remove_page(page_id=self.page.id)
        return super().setUp()

    def test_テキストを変更する(self):
        text_prop = Text.from_plain_text(name="テキスト", text="テスト")
        actual = update_page(page=self.page, property=text_prop)
        self.assertEqual(actual.get_text(name="テキスト").text, "テスト")

        text_empty_prop = Text.empty(name="テキスト")
        actual = update_page(page=self.page, property=text_empty_prop)
        self.assertEqual(actual.get_text(name="テキスト").text, "")

    def test_独自のテキストプロパティを作成する(self):
        # Given
        text_prop = OriginalText.from_plain_text(name="Text", text="テスト")
        self.assertIsInstance(text_prop, OriginalText)

        base_page = update_page(page=self.page, property=text_prop)
        actual: OriginalText = base_page.get(OriginalText)
        self.assertIsInstance(actual, OriginalText)
