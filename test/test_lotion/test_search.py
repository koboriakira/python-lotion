from unittest import TestCase

import pytest

from lotion.filter.builder import Builder
from lotion.filter.condition import Prop, Cond
from lotion import Lotion


@pytest.mark.api()
@pytest.mark.current()
class TestSearch(TestCase):
    DATABASE_ID = "15d6567a3bbf8032ada3e0a42892c357"

    def setUp(self) -> None:
        self.suite = Lotion.get_instance()
        return super().setUp()

    def test_検索_シンプルなテキスト検索(self):
        # Given
        filter_param = {
            "property": "テキスト",
            "rich_text": {
                "contains": "A",
            },
        }

        # When
        actual = self.suite.retrieve_database(
            database_id=self.DATABASE_ID,
            filter_param=filter_param,
        )

        # Then
        self.assertEqual(1, len(actual))

    def test_検索_複数の条件指定(self):
        # Given
        filter_param = (
            Builder.create()
            .add(Prop.RICH_TEXT, "名前", Cond.STARTS_WITH, "テスト")
            .add(Prop.NUMBER, "数値", Cond.GREATER_THAN, 50)
            .build()
        )

        # When
        actual = self.suite.retrieve_database(
            database_id=self.DATABASE_ID,
            filter_param=filter_param,
        )

        # Then
        self.assertEqual(1, len(actual))
