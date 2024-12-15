from unittest import TestCase

import pytest

from lotion import Lotion


@pytest.mark.api()
class TestSearch(TestCase):
    DATABASE_ID = "15d6567a3bbf8032ada3e0a42892c357"

    def setUp(self) -> None:
        self.suite = Lotion.get_instance()
        return super().setUp()

    def test_タイトルで検索する(self):
        # Given
        filter_param = {
            "property": "名前",
            "title": {
                "equals": "テストA",
            },
        }

        # When
        actual = self.suite.retrieve_database(
            database_id=self.DATABASE_ID,
            filter_param=filter_param,
        )

        # Then
        self.assertEqual(1, len(actual))
