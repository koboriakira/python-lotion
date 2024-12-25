from unittest import TestCase

import pytest

from lotion.block.rich_text.rich_text_builder import RichTextBuilder
from lotion.properties.text import Text
from lotion.properties.title import Title
from test.test_lotion.lotion_utils import create_empty_page, remove_page, update_page


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

    @pytest.mark.current()
    def test_タイトルを変更する(self) -> None:
        # Given
        rich_text = (
            RichTextBuilder.create()
            .add_text("prefix")
            .add_page_mention("1596567a3bbf80bb92a0d05094b0c110")
            .add_text("suffix")
            .build()
        )
        title = Title.from_rich_text(name="名前", rich_text=rich_text)

        # When
        actual = update_page(page=self.page, property=title)
        # Then
        self.assertEqual(actual.title, "prefixLotion開発用suffix")
